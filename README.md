# Panduan Dasar Flutter  
## Cara Membuat Flutter Apps dan Memahami Struktur Widget

---

# Daftar Isi

1. [Pendahuluan](#pendahuluan)  
2. [Persiapan dan Instalasi](#persiapan-dan-instalasi)  
3. [Membuat Project Flutter Lewat Terminal](#membuat-project-flutter-lewat-terminal)  
4. [Menjalankan Project Flutter](#menjalankan-project-flutter)  
5. [Struktur Dasar Project Flutter](#struktur-dasar-project-flutter)  
6. [Penjelasan File main.dart](#penjelasan-file-maindart)  
7. [Penjelasan Bagian per Bagian Kode](#penjelasan-bagian-per-bagian-kode)  
8. [Konsep Widget dalam Flutter](#konsep-widget-dalam-flutter)  
9. [Visible dan Invisible Widget](#visible-dan-invisible-widget)  
10. [Layout Widget: Row, Column, Stack](#layout-widget-row-column-stack)  
11. [Kesimpulan](#kesimpulan)

---

# Pendahuluan

Flutter adalah framework UI dari Google yang digunakan untuk membuat aplikasi:

- Android  
- iOS  
- Web  
- Desktop  

Flutter menggunakan bahasa Dart dan berbasis konsep Widget Tree.

---

# Persiapan dan Instalasi

Pastikan:

- Flutter sudah terinstal
- Dart sudah terinstal
- Emulator atau device tersedia

Cek instalasi:

```bash
flutter doctor
```

Pastikan tidak ada error.

---

# Membuat Project Flutter Lewat Terminal

## 1. Masuk ke Folder Tujuan

Contoh menyimpan project di D:/apps

```bash
cd ~
cd D:/apps
```

## 2. Membuat Direktori

```bash
md contoh_project
cd contoh_project
```

## 3. Membuat Project Flutter

```bash
flutter create project_apps
```

Perintah ini akan membuat struktur project Flutter lengkap.

---

# Menjalankan Project Flutter

Masuk ke folder project:

```bash
cd project_apps
```

Jalankan:

```bash
flutter run
```

Flutter akan melakukan build dan menampilkan demo default.

---

# Struktur Dasar Project Flutter

File utama berada di:

```
lib/main.dart
```

Struktur dasar aplikasi:

```
main()
 └── runApp()
      └── MyApp
           └── MaterialApp
                └── Scaffold
                     └── Body
```

---

# Penjelasan File main.dart

Contoh sederhana:

```dart
import 'package:flutter/material.dart';

void main () {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      home: Scaffold(
        backgroundColor: Colors.green,
        appBar: AppBar(
          backgroundColor: Color(0xffffff),
          title: Text("MyApps"),
        ),
        body: Center(
          child: Text("HALO"),
        ),
      ),
    );
  }
}
```

---

# Penjelasan Bagian per Bagian Kode

## Import

```dart
import 'package:flutter/material.dart';
```

Mengimpor library Material Design.

## main()

```dart
void main () {
  runApp(MyApp());
}
```

Titik awal program.

## StatelessWidget

```dart
class MyApp extends StatelessWidget
```

Widget tanpa state (tidak berubah).

## build()

```dart
Widget build(BuildContext context)
```

Method untuk membangun UI.

## MaterialApp

Kerangka utama aplikasi.

Properti penting:
- home
- theme
- routes
- debugShowCheckedModeBanner

## Scaffold

Struktur dasar halaman.

Bagian:
- appBar
- body
- backgroundColor
- floatingActionButton

## AppBar

Menampilkan bar bagian atas.

## Body

Isi utama halaman.

---

# Konsep Widget dalam Flutter

Semua di Flutter adalah widget.

Widget memiliki hubungan parent-child.

Contoh:

```
MaterialApp
 └── Scaffold
      └── Body
           └── Text
```

---

# Visible dan Invisible Widget

## Visible Widget

Widget yang terlihat di layar.

Contoh:
- Text
- AppBar
- Icon
- Image
- Container
- Button

## Invisible Widget

Widget yang tidak terlihat tetapi mengatur layout.

Contoh:
- Row
- Column
- Stack
- Center
- Padding

---

# Layout Widget: Row, Column, Stack

## Row (Horizontal)

```dart
body: Row(
  children: [
    Container(height: 50, width: 50, color: Colors.green),
    Container(height: 200, width: 50, color: Colors.blue),
    Container(height: 100, width: 50, color: Colors.red),
  ],
)
```

Row menyusun widget secara horizontal dari kiri ke kanan.

---

## Column (Vertical)

```dart
body: Column(
  children: [
    Container(width: 50, height: 50, color: Colors.green),
    Container(width: 200, height: 50, color: Colors.blue),
    Container(width: 100, height: 50, color: Colors.red),
  ],
)
```

Column menyusun widget secara vertikal dari atas ke bawah.

---

## Stack (Menumpuk)

```dart
body: Stack(
  children: [
    Container(height: 50, width: 50, color: Colors.green),
    Container(height: 200, width: 50, color: Colors.blue),
    Container(height: 100, width: 50, color: Colors.red),
  ],
)
```

Stack menumpuk widget satu di atas yang lain.

---

# Kesimpulan

- Flutter berbasis widget.
- Project dibuat dengan flutter create.
- File utama ada di lib/main.dart.
- Struktur dasar: main → runApp → MaterialApp → Scaffold → Body.
- Row, Column, dan Stack adalah widget layout penting.
