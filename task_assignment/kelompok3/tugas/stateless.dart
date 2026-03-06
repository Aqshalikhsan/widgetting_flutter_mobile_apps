import 'package:flutter/material.dart';

void main() {
  runApp(stl());
}

class stl extends StatelessWidget {
  const stl({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      home: Scaffold(
        body: Center(
          child: Row(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              Text(
                "violet",
                style: TextStyle(fontSize: 30, color: Colors.purple),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
