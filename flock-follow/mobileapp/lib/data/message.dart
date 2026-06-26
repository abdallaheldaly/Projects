import 'dart:convert';
import 'package:flock_follow/data/backend.dart';

class Message {
  int id;
  String content;
  DateTime createdAt;
  int userId;
  int flockId;

  Message.fromJson(Map<String, dynamic> json)
      : id = json['id'] as int,
        content = json['content'] as String,
        createdAt = DateTime.tryParse(json['created_at'] ?? ""),
        userId = json['user'] as int,
        flockId = json['flock'] as int;
}

Future<List<Message>> getFlockMessages(int flockId) async {
  final String data = await httpGet('flocks/$flockId/messages/');
  return parseMessages(data);
}

Message parseMessage(String responseText) {
  if (responseText == null || responseText.isEmpty) {
    return null;
  }

  final responseJson = json.decode(responseText);
  return Message.fromJson(responseJson);
}

List<Message> parseMessages(String responseText) {
  if (responseText == null || responseText.isEmpty) {
    return null;
  }

  final List responseJson = json.decode(responseText);
  return responseJson.map((jsonObject) => Message.fromJson(jsonObject)).toList();
}

Future<Message> createMessage(int flockId, int userId, String content) async {
  final String body = json.encode({
    'content': content,
    'user': userId,
  });
  final String res = await httpPost('flocks/$flockId/messages/', body);
  return parseMessage(res);
}
