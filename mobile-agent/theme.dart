import 'package:flutter/material.dart';

class JarvisTheme {
  static const Color primary = Color(0xFF00E5FF);
  static const Color surface = Color(0xFF111827);
  static const Color surfaceElevated = Color(0xFF1F2933);
  static const Color blackDeep = Color(0xFF0A0F14);
  static const Color whiteTech = Color(0xFFE6F7FF);

  static ThemeData get darkTheme {
    return ThemeData(
      brightness: Brightness.dark,
      scaffoldBackgroundColor: blackDeep,
      primaryColor: primary,
      cardColor: surface,
      textTheme: const TextTheme(
        bodyMedium: TextStyle(color: whiteTech, fontFamily: 'Inter'),
      ),
    );
  }
}
