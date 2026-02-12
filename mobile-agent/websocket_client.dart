import 'package:web_socket_channel/web_socket_channel.dart';

class JarvisWebSocket {
  late WebSocketChannel _channel;
  final String url;
  Function(String)? onMessage;

  JarvisWebSocket({required this.url});

  void connect() {
    _channel = WebSocketChannel.connect(Uri.parse(url));
    _channel.stream.listen((message) {
      if (onMessage != null) onMessage!(message);
    });
  }

  void sendMessage(String message) {
    _channel.sink.add(message);
  }

  void dispose() {
    _channel.sink.close();
  }
}
