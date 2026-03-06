import 'package:flutter/material.dart';

void main() {
  runApp(const MyApp());
}

// MyApp sekarang StatefulWidget supaya kita bisa ubah state kotak
class MyApp extends StatefulWidget {
  const MyApp({super.key});

  @override
  State<MyApp> createState() => _MyAppState(); //
}

class _MyAppState extends State<MyApp> {
  // State warna kotak untuk Row
  Color rowRed = Colors.red;
  Color rowYellow = Colors.yellow;
  Color rowBlue = Colors.blue;

  // State warna kotak untuk Column
List<Color> columnItems = [
  Colors.red,
  Colors.yellow,
  Colors.blue,
];

void tambahItemColumn() {
  setState(() {
    columnItems.add(
      Colors.primaries[columnItems.length % Colors.primaries.length],
    );
  });
}

  // State warna kotak untuk Stack
  Color stackRed = Colors.red;
  Color stackYellow = Colors.yellow;
  Color stackBlue = Colors.blue;

  // Fungsi toggle warna
  Color toggleColor(Color color) {
    if (color == Colors.red) return Colors.green;
    if (color == Colors.yellow) return Colors.orange;
    if (color == Colors.blue) return Colors.purple;
    return color;
  }

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      home: Scaffold(
        appBar: AppBar(
          backgroundColor: Colors.teal,
          title: const Text("Row, Column & Stack"),
        ),
        body: Padding(
          padding: const EdgeInsets.all(20.0),
          child: SingleChildScrollView(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                // 1️⃣ ROW
                const Text(
                  "1️⃣ Row (Horizontal Layout):",
                  style: TextStyle(fontWeight: FontWeight.bold),
                ),
                const SizedBox(height: 10),
                Row(
                  mainAxisAlignment: MainAxisAlignment.center,
                  children: [
                    GestureDetector(
                      onTap: () {
                        setState(() {
                          rowRed = toggleColor(rowRed);
                        });
                      },
                      child: Container(width: 60, height: 60, color: rowRed),
                    ),
                    const SizedBox(width: 10),
                    GestureDetector(
                      onTap: () {
                        setState(() {
                          rowYellow = toggleColor(rowYellow);
                        });
                      },
                      child: Container(width: 60, height: 60, color: rowYellow),
                    ),
                    const SizedBox(width: 10),
                    GestureDetector(
                      onTap: () {
                        setState(() {
                          rowBlue = toggleColor(rowBlue);
                        });
                      },
                      child: Container(width: 60, height: 60, color: rowBlue),
                    ),
                  ],
                ),
                const SizedBox(height: 30),

                // 2️⃣ COLUMN
                const Text(
                  "2️⃣ Column (Vertical Layout):",
                  style: TextStyle(fontWeight: FontWeight.bold),
                ),
                const SizedBox(height: 10),

                Column(
                  mainAxisSize: MainAxisSize.min,
                  children: columnItems.map((color) {
                    return Container(
                      margin: const EdgeInsets.only(bottom: 10),
                      width: 60,
                      height: 60,
                      color: color,
                    );
                  }).toList(),
                ),

                const SizedBox(height: 15),

                Center(
                  child: ElevatedButton(
                    onPressed: tambahItemColumn,
                    child: const Text("Tambah Item"),
                  ),
                ),

                const SizedBox(height: 30),

                // 3️⃣ STACK
                const Text(
                  "3️⃣ Stack (Menumpuk):",
                  style: TextStyle(fontWeight: FontWeight.bold),
                ),
                const SizedBox(height: 10),
                Stack(
                  alignment: Alignment.center,
                  children: [
                    GestureDetector(
                      onTap: () {
                        setState(() {
                          stackRed = toggleColor(stackRed);
                        });
                      },
                      child: Container(
                        width: 100,
                        height: 100,
                        color: stackRed,
                      ),
                    ),
                    GestureDetector(
                      onTap: () {
                        setState(() {
                          stackYellow = toggleColor(stackYellow);
                        });
                      },
                      child: Container(
                        width: 70,
                        height: 70,
                        color: stackYellow,
                      ),
                    ),
                    GestureDetector(
                      onTap: () {
                        setState(() {
                          stackBlue = toggleColor(stackBlue);
                        });
                      },
                      child: Container(width: 40, height: 40, color: stackBlue),
                    ),
                    const Text(
                      "Tengah",
                      style: TextStyle(
                        color: Colors.white,
                        fontWeight: FontWeight.bold,
                        shadows: [
                          Shadow(
                            color: Colors.black,
                            blurRadius: 5,
                            offset: Offset(0, 0),
                          ),
                        ],
                      ),
                    ),
                  ],
                ),
              ],
            ),
          ),
        ),
      ),
    );
  }
}
