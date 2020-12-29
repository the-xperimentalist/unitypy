import 'package:arcore_flutter_plugin/arcore_flutter_plugin.dart';
import 'package:flutter/material.dart';
// import 'package:arcore_flutter_plugin/arcore_flutter_plugin.dart';
import 'package:vector_math/vector_math_64.dart' as vector;
import "dart:io" as Io;
import 'dart:developer' as developer;
import 'package:flutter/services.dart';
// import 'package:http/http.dart' as http;
import 'dart:convert';


// class ArPage extends StatelessWidget {
//   @override
//   Widget build(BuildContext context) {
//     return Scaffold(
//       appBar: AppBar(
//         title: Text("Demo 2"),
//       ),
//       body: Container()
//     );
//   }
// }

class ArPage extends StatefulWidget {
  ArPage({Key key, this.title}) : super(key: key);
  final String title;

  @override
  _MyArPageState createState() => _MyArPageState();
}

class _MyArPageState extends State<ArPage> {
  ArCoreController arCoreController;
  ByteData imageData;
  Future _future;

  void loadImage() async {
    imageData = await rootBundle.load("assets/test_img.jpg");
  }

  // get rootBundle => null;

  @override
  void initState() {
    loadImage();
    super.initState();
  //   // rootBundle.load('test_img.jpg')
  //   //     .then((data) => setState(() => this.imageData = data));
  //   // NetworkImage()
  //   // http.Response response = await http.get(
  //   //   'https://cdn.pixabay.com/photo/2020/09/23/14/38/woman-5596173_960_720.jpg',
  //   // );
  //   // _base64 = base64Encode(response.bodyBytes);
  //   List<int> imageBytes = await widget.fileData.readAsBytes();
  }

  _onArCoreViewCreated(ArCoreController _arCoreController) {
    arCoreController = _arCoreController;
    _addSphere(arCoreController);
  }

  _addSphere(ArCoreController _arCoreController) {
    // final ByteData textureBytes = await rootBundle.load("assets/test_img.jpg");
    final material = ArCoreMaterial(color: Colors.deepOrange);
    // textureBytes: textureBytes.buffer.asUint8List());
    final sphere = ArCoreSphere(materials: [material], radius: 0.2);
    final node = ArCoreNode(shape: sphere, position: vector.Vector3(0, 0, -2),);
    _arCoreController.addArCoreNode(node);
  }

  Future _addCube(ArCoreController controller) async {

    final ByteData textureBytes = await rootBundle.load("assets/test_img.jpg");

    developer.log("In add cube");
    var file = Io.File('test_img.jpg');
    // developer.log("After io");
    var bytes = file.readAsBytes();
    // final ByteData bytes = await rootBundle.load('test_img.jpg');
    // var bytes2 = file.readAsBytesSync();
    // final bytes = Io.File("test_img.jpg").readAsBytesSync();
    // developer.log("After io 2");
    final material1 = ArCoreMaterial(
      color: Color.fromARGB(120, 66, 134, 244),
      metallic: 1.0,
      textureBytes: textureBytes.buffer.asUint8List()
    );
    final cube1 = ArCoreCube(
      materials: [material1],
      size: vector.Vector3(1, 1, 0.01),
    );
    final material2 = ArCoreMaterial(
      color: Color.fromARGB(120, 66, 134, 244),
      metallic: 1.0,
    );
    final cube2 = ArCoreCube(
      materials: [material1],
      size: vector.Vector3(1, 1, 0.01),
    );
    final material3 = ArCoreMaterial(
      color: Color.fromARGB(120, 66, 134, 244),
      metallic: 1.0,
    );
    final cube3 = ArCoreCube(
      materials: [material1],
      size: vector.Vector3(1, 1, 0.01),
    );
    final node1 = ArCoreNode(
      shape: cube1,
      position: vector.Vector3(-0.5, 0.5, -3.5),
    );
    final node2 = ArCoreNode(
      shape: cube2,
      position: vector.Vector3(-1.0, 1.0, -2.5),
    );
    final node3 = ArCoreNode(
      shape: cube3,
      position: vector.Vector3(1.5, -0.5, -2.5),
    );
    controller.addArCoreNode(node1);
    controller.addArCoreNode(node2);
    controller.addArCoreNode(node3);
  }

  _addCubeWithImage(ArCoreController _arCoreController) {
    var file = Io.File('test_img.jpg');
    final bytes = Io.File("test_img.jpg").readAsBytesSync();
    final material = ArCoreMaterial(color: Colors.deepOrange, textureBytes: bytes);
    final cube = ArCoreCube(size: vector.Vector3(3, 3, 3), materials: [material]);
    final node = ArCoreNode(shape: cube, position: vector.Vector3(0, 0, 0),);
    _arCoreController.addArCoreNode(node);
  }

  _addImage(ArCoreController _arCoreController) {
    var file = Io.File('test_img.jpg');
    final bytes = Io.File("test_img.jpg").readAsBytesSync();
    final image = ArCoreImage(bytes: bytes, width: 100, height: 100);

    final node = ArCoreNode(image: image, position: vector.Vector3(0, 0, -2));
    _arCoreController.addArCoreNode(node);
  }

  @override
  Widget build(BuildContext context) {
    // if (imageData == null) {
    //   return Center(child: CircularProgressIndicator(),);
    // }
    return Scaffold(
      appBar: AppBar(
        title: Text("Ar Page"),
      ),
      body: ArCoreView(onArCoreViewCreated: _onArCoreViewCreated,),
    );
  }
}
