import 'package:example/modules/help_screen.dart';
import 'package:example/modules/home_screen.dart';
import 'package:example/modules/settings_screen.dart';
import 'package:flutter/material.dart';
import 'package:flux_scaffold/flux_scaffold.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(home: MyWidget(), debugShowCheckedModeBanner: false);
  }
}

class MyWidget extends StatelessWidget {
  const MyWidget({super.key});

  @override
  Widget build(BuildContext context) {
    return TabScaffold(
      // marginNavButtonBar: EdgeInsets.only(left: 20, right: 20),
      // backgroundImage: "assets/Images/b.jpeg",
      // topNavButtonBar: true,
      nested: true,
      paddingValue: 10,
      numberTab: 3,
      pages: [HomeScreen(), HelpScreen(), SettingsScreen()],
      bottomNavItems: [
        BottomNavItem(icon: Icons.home, label: "Home"),
        BottomNavItem(icon: Icons.help, label: "Help"),
        BottomNavItem(icon: Icons.help, label: "Help"),
      ],
      navigationBarBg: Colors.amber[100],
    );
  }
}
