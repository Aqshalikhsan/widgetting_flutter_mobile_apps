import 'package:flutter/material.dart';
import 'widget/ProductCart.dart';
import 'widget/StackProductBanner.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Katalog Produk',
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(seedColor: Colors.blue),
        useMaterial3: true,
      ),
      home: const MyHomePage(title: 'Dashboard Produk'),
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
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Theme.of(context).colorScheme.inversePrimary,
        title: Text(widget.title),
      ),

      body: SingleChildScrollView(
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            const Padding(
              padding: EdgeInsets.all(16.0),
              child: Text(
                "10 Produk Terlaris",
                style: TextStyle(
                  fontSize: 20,
                  fontWeight: FontWeight.bold,
                  color: Colors.black87,
                ),
              ),
            ),
            SingleChildScrollView(
              scrollDirection: Axis.horizontal,
              padding: const EdgeInsets.all(16.0),
              child: Row(
                children: const [
                  ProductCard(
                    name: "Susu UHT Cokelat",
                    barcode: "89912341",
                    stock: 12,
                    expiryDate: "12/12/2026",
                  ),
                  SizedBox(width: 12),
                  ProductCard(
                    name: "Gula Pasir 1kg",
                    barcode: "89955442",
                    stock: 5,
                    expiryDate: "01/05/2027",
                  ),
                  SizedBox(width: 12),
                  ProductCard(
                    name: "Kopi Arabica",
                    barcode: "89900113",
                    stock: 50,
                    expiryDate: "20/10/2026",
                  ),
                ],
              ),
            ),

            const Padding(
              padding: EdgeInsets.all(16.0),
              child: Text(
                "Promo Spesial",
                style: TextStyle(fontSize: 20, fontWeight: FontWeight.bold),
              ),
            ),

            Card(
              margin: const EdgeInsets.symmetric(horizontal: 16, vertical: 8),
              child: ListTile(
                leading: const Icon(Icons.local_offer, color: Colors.red),
                title: const Text("Diskon 50% - Susu UHT"),
                subtitle: const Text("Berlaku sampai 30 Maret"),
                trailing: const Icon(Icons.arrow_forward),
              ),
            ),
            Card(
              margin: const EdgeInsets.symmetric(horizontal: 16, vertical: 8),
              child: ListTile(
                leading: const Icon(Icons.local_offer, color: Colors.red),
                title: const Text("Beli 1 Gratis 1 - Kopi Arabica"),
                subtitle: const Text("Stok terbatas!"),
                trailing: const Icon(Icons.arrow_forward),
              ),
            ),

            const Padding(
              padding: EdgeInsets.all(16.0),
              child: Text(
                "Produk Unggulan",
                style: TextStyle(fontSize: 20, fontWeight: FontWeight.bold),
              ),
            ),

            const StackProductBanner(),

            Padding(
              padding: EdgeInsets.symmetric(horizontal: 16),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Text(
                    "Rekomendasi Untuk Kamu",
                    style: TextStyle(fontSize: 20, fontWeight: FontWeight.bold),
                  ),

                  SizedBox(height: 10),

                  SingleChildScrollView(
                    scrollDirection: Axis.horizontal,
                    child: Row(
                      children: [
                        ProductCard(
                          name: "Teh Botol",
                          barcode: "88991234",
                          stock: 20,
                          expiryDate: "10/11/2026",
                        ),

                        SizedBox(width: 12),

                        ProductCard(
                          name: "Air Mineral",
                          barcode: "88995544",
                          stock: 15,
                          expiryDate: "05/02/2027",
                        ),

                        SizedBox(width: 12),

                        ProductCard(
                          name: "Minum Isotonik",
                          barcode: "88997766",
                          stock: 8,
                          expiryDate: "12/09/2026",
                        ),
                      ],
                    ),
                  ),

                  SizedBox(height: 20),
                ],
              ),
            ),
          ],
        ),
      ),
    );
  }
}
