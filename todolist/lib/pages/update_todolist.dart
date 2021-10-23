import 'package:flutter/material.dart';
// http method package
import 'package:http/http.dart' as http;
import 'dart:async';
import 'dart:convert';

class UpdatePage extends StatefulWidget {
  final v1, v2, v3;
  const UpdatePage(this.v1, this.v2, this.v3);

  @override
  _UpdatePageState createState() => _UpdatePageState();
}

class _UpdatePageState extends State<UpdatePage> {
  var _v1, _v2, _v3;
  TextEditingController todo_title = TextEditingController();
  TextEditingController todo_detail = TextEditingController();

  @override
  void initState() {
    // TODO: implement initState
    super.initState();
    _v1 = widget.v1; // id
    _v2 = widget.v2; // title
    _v3 = widget.v3; // detail
    todo_title.text = _v2;
    todo_detail.text = _v3;
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('ແກ້ໄຂ'),
        actions: [
          IconButton(
              onPressed: () {
                print("Delete ID: $_v1");
                deleteTodo();
                Navigator.pop(context, 'delete'); // ຄືການກົດ back <--
              },
              icon: Icon(
                Icons.delete,
                color: Colors.red[800],
              ))
        ],
      ),
      body: Padding(
        padding: const EdgeInsets.all(20),
        child: ListView(
          children: [
            // ຊ່ອງໃສ່ຂໍ້ມູນ title
            TextField(
                controller: todo_title,
                decoration: InputDecoration(
                    labelText: 'ລາຍການທີ່ຕ້ອງເຮັດ',
                    border: OutlineInputBorder())),
            SizedBox(
              height: 30,
            ),
            TextField(
                minLines: 4,
                maxLines: 8,
                controller: todo_detail,
                decoration: InputDecoration(
                    labelText: 'ລາຍລະອຽດ', border: OutlineInputBorder())),
            SizedBox(
              height: 30,
              // ປຸ່ມເພີ່ມຂໍ້ມູນ
            ),
            Padding(
              padding: const EdgeInsets.all(20),
              child: ElevatedButton(
                onPressed: () {
                  print('----------');
                  print('title: ${todo_title.text}');
                  print('detail: ${todo_detail.text}');
                  updateTodo();
                  final snackBar = SnackBar(
                    content: const Text('ອັພເດຕລາຍການສຳເລັດແລ້ວ'),
                  );

                  ScaffoldMessenger.of(context).showSnackBar(snackBar);
                },
                child: Text("ແກ້ໄຂ"),
                style: ButtonStyle(
                    backgroundColor:
                        MaterialStateProperty.all(Colors.blueAccent[700]),
                    padding: MaterialStateProperty.all(
                        EdgeInsets.fromLTRB(50, 20, 50, 20)),
                    textStyle:
                        MaterialStateProperty.all(TextStyle(fontSize: 30))),
              ),
            ),
          ],
        ),
      ),
    );
  }

  Future updateTodo() async {
    //'api.bitkub.com','/api/market/ticker'
    //var url = Uri.https('a2c4-115-84-96-27.ngrok.io', '/api/post-todolist');
    var url = Uri.http('192.168.0.54:8000', '/api/update-todolist/$_v1');
    Map<String, String> header = {"Content-type": "application/json"};
    String jsondata =
        '{"title":"${todo_title.text}","detail":"${todo_detail.text}"}';
    var response = await http.put(url, headers: header, body: jsondata);
    print('------result------');
    print(response.body);
  }

  Future deleteTodo() async {
    var url = Uri.http('192.168.0.54:8000', '/api/delete-todolist/$_v1');
    Map<String, String> header = {"Content-type": "application/json"};
    var response = await http.delete(url, headers: header);
    print('------result------');
    print(response.body);
  }
}
