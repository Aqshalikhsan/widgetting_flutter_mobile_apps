# Panduan Dasar Flutter
## Cara Membuat Flutter Apps dan Memahami Struktur Widget

---

# Daftar Isi

1. [Pendahuluan](#pendahuluan)
2. [Apa Itu Flutter?](#apa-itu-flutter)
3. [Konsep Dasar: Widget Tree](#konsep-dasar-widget-tree)
4. [Membuat Project Flutter Lewat Terminal](#membuat-project-flutter-lewat-terminal)
5. [Menjalankan Project Flutter](#menjalankan-project-flutter)
6. [Struktur Dasar Project Flutter](#struktur-dasar-project-flutter)
7. [Penjelasan File main.dart](#penjelasan-file-maindart)
8. [Penjelasan Detail Tiap Bagian Kode](#penjelasan-detail-tiap-bagian-kode)
9. [StatelessWidget dan StatefulWidget](#statelesswidget-dan-statefulwidget)
10. [Visible dan Invisible Widget](#visible-dan-invisible-widget)
11. [Layout Widget: Row, Column, Stack](#layout-widget-row-column-stack)
12. [Kesimpulan](#kesimpulan)

---

# Pendahuluan

Dokumentasi ini bertujuan untuk menjelaskan dasar pembuatan aplikasi Flutter mulai dari terminal hingga memahami struktur utama `main.dart`, termasuk konsep widget dan layout.

Materi ini cocok untuk:
- Pemula
- Mahasiswa semester awal
- Siswa SMK RPL
- Bootcamp dasar Flutter

---

# Apa Itu Flutter?

Flutter adalah framework UI (User Interface) dari Google yang digunakan untuk membangun aplikasi lintas platform menggunakan satu basis kode (single codebase).

Platform yang didukung:
- Android
- iOS
- Web
- Desktop

Flutter menggunakan bahasa pemrograman Dart.

Keunggulan Flutter:
- Hot Reload (perubahan langsung terlihat)
- Performa tinggi
- UI fleksibel
- Berbasis Widget

---

# Konsep Dasar: Widget Tree

Flutter sepenuhnya berbasis widget.

Semua yang ada di layar adalah widget, termasuk:
- Teks
- Tombol
- Layout
- Bahkan aplikasi itu sendiri

Struktur Flutter berbentuk pohon (tree):

```
MaterialApp
 └── Scaffold
      └── Body
           └── Text
```

Konsep Parent–Child:
- Widget bisa memiliki anak (children)
- Parent mengatur posisi dan perilaku child

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

Penjelasan:
- `md` untuk membuat folder
- `cd` untuk berpindah folder

## 3. Membuat Project Flutter

```bash
flutter create project_apps
```

Perintah ini akan:
- Membuat struktur project lengkap
- Membuat file `main.dart`
- Mengatur dependency default
- Membuat folder Android, iOS, Web, dll

---

# Menjalankan Project Flutter

Masuk ke folder project:

```bash
cd project_apps
```

Jalankan aplikasi:

```bash
flutter run
```

Penjelasan:
- Flutter akan melakukan build
- Menghubungkan ke emulator/device
- Menampilkan Flutter Demo bawaan

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

Penjelasan:

- `main()` adalah titik awal program
- `runApp()` menjalankan root widget
- `MaterialApp` adalah kerangka aplikasi
- `Scaffold` adalah struktur halaman
- `Body` adalah isi utama halaman

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

# Penjelasan Detail Tiap Bagian Kode

## 1. Import

```dart
import 'package:flutter/material.dart';
```

Mengimpor library Material Design yang berisi widget bawaan seperti:
- MaterialApp
- Scaffold
- AppBar
- Text
- Container

Tanpa import ini, widget tersebut tidak dapat digunakan.

---

## 2. Fungsi main()

```dart
void main () {
  runApp(MyApp());
}
```

Pengertian:
- Fungsi pertama yang dijalankan saat aplikasi dimulai
- `runApp()` menjalankan widget utama

---

## 3. StatelessWidget

```dart
class MyApp extends StatelessWidget
```

Pengertian:
StatelessWidget adalah widget yang tidak memiliki state (data yang berubah).

Karakteristik:
- UI bersifat tetap
- Tidak menggunakan `setState()`
- Cocok untuk tampilan statis

---

## 4. Method build()

```dart
Widget build(BuildContext context)
```

Pengertian:
Method yang digunakan untuk membangun dan mengembalikan tampilan UI.

Setiap kali widget perlu diperbarui, method build akan dipanggil kembali.

---

## 5. MaterialApp

Pengertian:
MaterialApp adalah widget yang menjadi kerangka utama aplikasi berbasis Material Design.

Fungsi:
- Mengatur tema
- Mengatur navigasi
- Menentukan halaman awal

Properti penting:
- `home` → halaman pertama
- `theme` → pengaturan warna
- `routes` → navigasi antar halaman
- `debugShowCheckedModeBanner` → menampilkan atau menyembunyikan label debug

---

## 6. Scaffold

Pengertian:
Scaffold adalah struktur dasar halaman dalam Flutter.

Fungsi:
- Menyediakan layout standar aplikasi
- Mengatur bagian AppBar, Body, Drawer, dan lainnya

Bagian penting:
- `appBar`
- `body`
- `backgroundColor`
- `floatingActionButton`

---

## 7. AppBar

Pengertian:
Widget yang menampilkan bar di bagian atas aplikasi.

Biasanya berisi:
- Judul
- Icon
- Tombol navigasi

---

## 8. Body

Pengertian:
Bagian utama dari halaman yang menampilkan konten aplikasi.

Contoh:

```dart
body: Center(
  child: Text("HALO"),
)
```

- `Center` memposisikan widget di tengah
- `Text` menampilkan teks

---

# StatelessWidget dan StatefulWidget

## StatelessWidget

- Tidak memiliki state
- UI tidak berubah
- Cocok untuk tampilan tetap

## StatefulWidget

- Memiliki state (data bisa berubah)
- Menggunakan `setState()`
- Cocok untuk:
  - Counter
  - Form input
  - Animasi

State adalah data yang dapat berubah selama aplikasi berjalan.

---

# Visible dan Invisible Widget

## Visible Widget

Pengertian:
Widget yang terlihat secara visual di layar.

Contoh:
- Text
- Icon
- Image
- Button
- Container dengan warna

Fungsi:
Menampilkan elemen UI kepada pengguna.

---

## Invisible Widget

Pengertian:
Widget yang tidak terlihat secara visual, tetapi mengatur tata letak.

Contoh:
- Row
- Column
- Stack
- Center
- Padding
- Expanded

Fungsi:
Mengatur posisi dan susunan widget lain.

---

# Layout Widget: Row, Column, Stack

## Row

Pengertian:
Widget layout yang menyusun child secara horizontal (kiri ke kanan).

Contoh:

```dart
body: Row(
  children: [
    Container(height: 50, width: 50, color: Colors.green),
    Container(height: 200, width: 50, color: Colors.blue),
    Container(height: 100, width: 50, color: Colors.red),
  ],
)
```

Properti penting:
- `mainAxisAlignment`
- `crossAxisAlignment`

---

## Column

Pengertian:
Widget layout yang menyusun child secara vertikal (atas ke bawah).

Contoh:

```dart
body: Column(
  children: [
    Container(width: 50, height: 50, color: Colors.green),
    Container(width: 200, height: 50, color: Colors.blue),
    Container(width: 100, height: 50, color: Colors.red),
  ],
)
```

---

## Stack

Pengertian:
Widget layout yang menumpuk child satu di atas yang lain.

Contoh:

```dart
body: Stack(
  children: [
    Container(height: 50, width: 50, color: Colors.green),
    Container(height: 200, width: 50, color: Colors.blue),
    Container(height: 100, width: 50, color: Colors.red),
  ],
)
```

Child terakhir akan berada paling atas.

Biasanya digunakan untuk:
- Overlay
- Badge notifikasi
- Background dengan teks di atasnya

---

# Kesimpulan

- Flutter adalah framework UI berbasis widget.
- Semua elemen dalam Flutter adalah widget.
- Struktur dasar aplikasi: main → runApp → MaterialApp → Scaffold → Body.
- StatelessWidget digunakan untuk tampilan tetap.
- StatefulWidget digunakan untuk tampilan yang berubah.
- Row, Column, dan Stack adalah layout dasar yang wajib dipahami.

Memahami konsep widget dan struktur dasar adalah fondasi untuk mengembangkan aplikasi Flutter yang lebih kompleks.
