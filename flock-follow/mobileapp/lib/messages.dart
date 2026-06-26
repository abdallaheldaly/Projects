import 'dart:async';

import 'package:flutter/material.dart';

import 'data/app_status.dart';
import 'data/member.dart';
import 'data/message.dart';
import 'data/user.dart';
import 'utilities.dart';

class MessagesPage extends StatefulWidget {
  final AppStatus appStatus;

  const MessagesPage(this.appStatus, {Key key}) : super(key: key);

  @override
  _MessagesPage createState() => _MessagesPage();
}

class _MessagesPage extends State<MessagesPage> {
  static const _pollInterval = Duration(seconds: 5);

  final List<Message> _messages = <Message>[];
  final Map<int, User> _membersById = <int, User>{};
  final TextEditingController _textController = TextEditingController();
  Timer _pollTimer;
  bool _isSending = false;
  bool _isRefreshing = false;

  @override
  void initState() {
    super.initState();
    WidgetsBinding.instance.addPostFrameCallback((_) => _refresh());
    _pollTimer = Timer.periodic(_pollInterval, (_) => _refresh());
  }

  @override
  void dispose() {
    _pollTimer?.cancel();
    _textController.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Colors.green,
        title: Text('Messages'),
      ),
      body: Column(
        children: <Widget>[
          Flexible(
            child: _messages.isEmpty
                ? Center(child: Text('No messages yet. Say hello!'))
                : ListView.builder(
                    reverse: true,
                    padding: EdgeInsets.all(8.0),
                    itemCount: _messages.length,
                    itemBuilder: (_, index) =>
                        _buildMessageTile(_messages[_messages.length - 1 - index]),
                  ),
          ),
          Divider(height: 1.0),
          _buildComposer(),
        ],
      ),
    );
  }

  Widget _buildMessageTile(Message message) {
    final bool isMe = message.userId == widget.appStatus.user.id;
    final User sender = _membersById[message.userId];
    final String senderName = sender?.name ?? 'Unknown';

    return Container(
      margin: const EdgeInsets.symmetric(vertical: 6.0),
      child: Row(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: <Widget>[
          Container(
            margin: const EdgeInsets.only(right: 12.0),
            child: CircleAvatar(
              child: Text(senderName.isEmpty ? '?' : senderName[0].toUpperCase()),
            ),
          ),
          Expanded(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: <Widget>[
                Text(
                  isMe ? 'You' : senderName,
                  style: Theme.of(context).textTheme.subtitle1,
                ),
                Container(
                  margin: const EdgeInsets.only(top: 4.0),
                  child: Text(message.content),
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }

  Widget _buildComposer() {
    return Container(
      margin: const EdgeInsets.symmetric(horizontal: 9.0, vertical: 6.0),
      child: Row(
        children: <Widget>[
          Flexible(
            child: TextField(
              controller: _textController,
              enabled: !_isSending,
              decoration: InputDecoration.collapsed(hintText: "Type a message"),
              onSubmitted: (_) => _submitMessage(),
            ),
          ),
          IconButton(
            icon: Icon(Icons.send),
            onPressed: _isSending ? null : _submitMessage,
          ),
        ],
      ),
    );
  }

  Future _submitMessage() async {
    final text = _textController.text.trim();
    if (text.isEmpty) return;

    setState(() => _isSending = true);
    try {
      await createMessage(widget.appStatus.flock.id, widget.appStatus.user.id, text);
      _textController.clear();
      await _loadMessages();
    }
    catch (ex) {
      if (mounted) await showAlert(context, ex, "Sending message failed");
    }
    finally {
      if (mounted) setState(() => _isSending = false);
    }
  }

  Future _refresh() async {
    if (_isRefreshing) return;
    _isRefreshing = true;
    try {
      await _loadMembers();
      await _loadMessages();
    }
    finally {
      _isRefreshing = false;
    }
  }

  Future _loadMembers() async {
    try {
      final members = await getFlockMembers(widget.appStatus.flock.id);
      if (!mounted) return;
      setState(() {
        _membersById.clear();
        for (final member in members) {
          _membersById[member.id] = member;
        }
      });
    }
    catch (ex) {
      // Member names are a nice-to-have for chat; don't interrupt the user
      // with an alert just because this background refresh failed.
      print('Failed to load flock members: $ex');
    }
  }

  Future _loadMessages() async {
    try {
      final messages = await getFlockMessages(widget.appStatus.flock.id);
      if (!mounted) return;
      setState(() => _messages
        ..clear()
        ..addAll(messages));
    }
    catch (ex) {
      print('Failed to load messages: $ex');
    }
  }
}
