import 'package:flutter/material.dart';

class ProductCard extends StatelessWidget {
  final String name;
  final String barcode;
  final int stock;
  final String expiryDate;

  const ProductCard({
    super.key,
    required this.name,
    required this.barcode,
    required this.stock,
    required this.expiryDate,
  });

  @override
  Widget build(BuildContext context) {
    return Card(
      elevation: 4,
      shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(15)),
      child: Container(
        width: 250,
        padding: const EdgeInsets.all(12),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          mainAxisSize: MainAxisSize.min,
          children: [
            Text(
              name,
              style: const TextStyle(fontSize: 18, fontWeight: FontWeight.bold),
              maxLines: 1,
              overflow: TextOverflow.ellipsis,
            ),

            const SizedBox(height: 4),

            Container(
              padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 4),
              decoration: BoxDecoration(
                color: Colors.grey[100],
                borderRadius: BorderRadius.circular(4),
              ),
              child: Row(
                children: [
                  const Icon(Icons.qr_code_2, size: 20, color: Colors.black87),
                  const SizedBox(width: 8),
                  Text(
                    barcode,
                    style: const TextStyle(fontFamily: 'Courier', fontSize: 13),
                  ),
                ],
              ),
            ),

            const Divider(height: 20),

            Row(
              mainAxisAlignment: MainAxisAlignment.spaceAround,
              children: [
                _buildInfoColumn("Stok", "$stock Pcs", Colors.blue),
                _buildInfoColumn("Kadaluarsa", expiryDate, Colors.redAccent),
              ],
            ),
          ],
        ),
      ),
    );
  }

  Widget _buildInfoColumn(String label, String value, Color color) {
    return Column(
      children: [
        Text(label, style: const TextStyle(fontSize: 11, color: Colors.grey)),
        Text(
          value,
          style: TextStyle(
            fontSize: 13,
            fontWeight: FontWeight.bold,
            color: color,
          ),
        ),
      ],
    );
  }
}
