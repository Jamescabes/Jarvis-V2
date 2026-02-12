import 'package:flutter/material.dart';
import 'theme.dart';

class ChatScreen extends StatefulWidget {
  const ChatScreen({super.key});

  @override
  State<ChatScreen> createState() => _ChatScreenState();
}

class _ChatScreenState extends State<ChatScreen> {
  final List<Map<String, dynamic>> _messages = [
    {'text': 'Señor, el sistema está operativo. ¿En qué puedo ayudarle?', 'isJarvis': true},
  ];

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Jarvis', style: TextStyle(color: JarvisTheme.primary, fontWeight: FontWeight.bold)),
        backgroundColor: JarvisTheme.blackDeep,
        centerTitle: true,
      ),
      body: Column(
        children: [
          Expanded(
            child: ListView.builder(
              padding: const EdgeInsets.all(16),
              itemCount: _messages.length,
              itemBuilder: (context, index) {
                final msg = _messages[index];
                return Align(
                  alignment: msg['isJarvis'] ? Alignment.centerLeft : Alignment.centerRight,
                  child: Container(
                    margin: const EdgeInsets.symmetric(vertical: 8),
                    padding: const EdgeInsets.all(12),
                    decoration: BoxDecoration(
                      color: msg['isJarvis'] ? JarvisTheme.surfaceElevated : JarvisTheme.primary.withOpacity(0.1),
                      borderRadius: BorderRadius.circular(12),
                      border: msg['isJarvis'] ? null : Border.all(color: JarvisTheme.primary.withOpacity(0.3)),
                    ),
                    child: Text(msg['text']),
                  ),
                );
              },
            ),
          ),
          _buildInputArea(),
        ],
      ),
    );
  }

  Widget _buildInputArea() {
    return Container(
      padding: const EdgeInsets.all(16),
      color: JarvisTheme.surface,
      child: Row(
        children: [
          Expanded(
            child: TextField(
              decoration: InputDecoration(
                hintText: 'Diga algo, señor...',
                fillColor: JarvisTheme.blackDeep,
                filled: true,
                border: OutlineInputBorder(borderRadius: BorderRadius.circular(20), borderSide: BorderSide.none),
              ),
            ),
          ),
          const SizedBox(width: 8),
          CircleAvatar(
            backgroundColor: JarvisTheme.primary,
            child: IconButton(
              icon: const Icon(Icons.mic, color: Colors.black),
              onPressed: () {},
            ),
          ),
        ],
      ),
    );
  }
}
