import 'package:flutter/material.dart';

void main() {
  runApp(const stf());
}

class stf extends StatefulWidget {
  const stf({super.key});

  @override
  State<stf> createState() => _stfState();
}

class _stfState extends State<stf> {
  int angka = 0;
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      home: Scaffold(
        body: Center(
          child: Column(
            mainAxisSize: MainAxisSize.min,
            children: [
              Text(
                "Angka: $angka",
                style: TextStyle(fontSize: 20, color: Colors.blue),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
