import 'dart:convert';

import 'backend.dart';

class Flock {
  int id;
  String title;
  String description;
  String status;
  String password;
  String destination;
  double latitude;
  double longitude;
  DateTime createdAt;
  DateTime startedAt;
  DateTime finishedAt;
  int leaderId;

  Flock.fromJson(Map<String, dynamic> json):
        id = json['id'] as int,
        title = json['title'] as String,
        description = json['description'] as String,
        status = json['status'] as String,
        // The backend never returns the password (it's write_only), so this
        // will normally be null here. We only ever read it back off a Flock
        // we created ourselves in this session (see createFlock below).
        password = json['password'] as String,
        destination = json['destination'] as String,
        latitude = double.tryParse(json['latitude'] ?? ""),
        longitude = double.tryParse(json['longitude'] ?? ""),
        createdAt = DateTime.tryParse(json["created_at"]),
        startedAt = DateTime.tryParse(json["started_at"] ?? ""),
        finishedAt = DateTime.tryParse(json["finished_at"] ?? ""),
        leaderId = json['leader'] as int;

  String get flockStatus {
    switch (status) {
      case 'C': return "Created";
      case 'S': return "Started";
      case 'F': return "Finished";
      default: return "Unknown";
    }
  }
}

Future<Flock> readFlock(id) async {
  final String data = await httpGet("flocks/$id/");
  return parseFlock(data);
}

Future<List<Flock>> findFlocks(double lat, double lng) async {
  final String data = await httpGet("flocks/", {
    "lat": lat.toString(), "lng": lng.toString()
  });
  return parseFlocks(data);
}

Flock parseFlock(String responseText) {
  if (responseText == null || responseText.isEmpty) {
    return null;
  }

  final responseJson = json.decode(responseText);
  return Flock.fromJson(responseJson);
}

List<Flock> parseFlocks(String responseText) {
  if (responseText == null || responseText.isEmpty) {
    return null;
  }

  final List responseJson = json.decode(responseText);
  return responseJson.map((jsonObject) => Flock.fromJson(jsonObject)).toList();
}

Future<Flock> createFlock(
    String title,
    String destination,
    String password,
    double latitude,
    double longitude,
    int leaderId,
    ) async {
  final String body = json.encode({
    'title': title,
    'destination': destination,
    'password': password,
    'latitude': latitude.toString(),
    'longitude': longitude.toString(),
    'leader': leaderId,
  });
  final String res = await httpPost('flocks/', body);
  final Flock flock = parseFlock(res);
  // The backend never echoes the password back (it's write_only), so keep
  // hold of the value the leader just chose for later use (e.g. showing it
  // again, or re-sending it on a future join from this same device).
  flock.password = password;
  return flock;
}

Future updateFlock(Flock flock) async {
  final String body = json.encode({
    'id': flock.id,
    'title': flock.title,
    'destination': flock.destination,
    'latitude': flock.latitude.toString(),
    'longitude': flock.longitude.toString(),
    'status': flock.status,
    'leader': flock.leaderId,
  });
  await httpPut('flocks/${flock.id}/', body);
}
