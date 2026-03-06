import 'package:flutter/material.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Stateful Demo',
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(
          seedColor: const Color.fromARGB(255, 58, 183, 96),
        ),
        useMaterial3: true,
      ),
      home: const MyHomePage(title: 'Contoh Stateful'),
    );
  }
}

class MyHomePage extends StatefulWidget {
  const MyHomePage({super.key, required this.title});
  final String title;

  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  int _counter = 0;

  void _tambah() {
    setState(() {
      _counter++;
    });
  }

  void _kurang() {
    setState(() {
      _counter--;
    });
  }

  void _reset() {
    setState(() {
      _counter = 0;
    });
  }

  void _simpan() {
    ScaffoldMessenger.of(
      context,
    ).showSnackBar(SnackBar(content: Text('Angka disimpan: $_counter')));
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Theme.of(context).colorScheme.inversePrimary,
        title: Text(widget.title),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            // ================== STATELESS ==================
            const TulisanStateless(),

            const SizedBox(height: 20),

            // ================== STATEFUL ==================
            const Text(
              'INI ADALAH CONTOH STATEFUL',
              style: TextStyle(
                color: Colors.red,
                fontSize: 18,
                fontWeight: FontWeight.bold,
              ),
            ),

            const SizedBox(height: 20),

            const Text(
              'Jumlah Angka Saat Ini:',
              style: TextStyle(fontSize: 16),
            ),

            Text(
              '$_counter',
              style: Theme.of(context).textTheme.headlineMedium,
            ),

            const SizedBox(height: 20),

            Row(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                ElevatedButton(onPressed: _kurang, child: const Text('-')),
                const SizedBox(width: 10),
                ElevatedButton(onPressed: _reset, child: const Text('Reset')),
                const SizedBox(width: 10),
                ElevatedButton(onPressed: _tambah, child: const Text('+')),
              ],
            ),

            const SizedBox(height: 10),

            // ================== TOMBOL SIMPAN ==================
            ElevatedButton(onPressed: _simpan, child: const Text('Simpan')),

            const SizedBox(height: 10),

            Text(
              'Nilai terakhir adalah $_counter',
              style: const TextStyle(
                fontSize: 16,
                color: Colors.green,
                fontWeight: FontWeight.w500,
              ),
            ),
          ],
        ),
      ),
    );
  }
}

class TulisanStateless extends StatelessWidget {
  const TulisanStateless({super.key});

  @override
  Widget build(BuildContext context) {
    return const Text(
      'INI MERUPAKAN TUGAS DARI KELOMPOK 3 GOLONGAN E',
      style: TextStyle(
        color: Colors.blue,
        fontSize: 18,
        fontWeight: FontWeight.bold,
      ),
    );
  }
}
