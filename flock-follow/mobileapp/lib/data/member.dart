
import 'dart:convert';

import 'backend.dart';
import 'user.dart';

Future joinFlock(int flockId, int userId, [String password]) async {
  final String body = json.encode({'password': password ?? ''});
  await httpPost('flocks/$flockId/members/$userId/', body);
}

Future<List<User>> getFlockMembers(int flockId) async {
  final String data = await httpGet('flocks/$flockId/members/');
  return parseUsers(data);
}

Future leaveFlock(int flockId, int userId) async {
  await httpDelete('flocks/$flockId/members/$userId/');
}
