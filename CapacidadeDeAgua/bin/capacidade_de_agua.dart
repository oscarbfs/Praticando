import 'package:capacidade_de_agua/capacidade_de_agua.dart' as ca;

void main(List<String> arguments) {
  List<int> box1 = [3,0,3]; // 3
  List<int> box2 = [0,0,3]; // 0
  List<int> box3 = [3,0,0]; // 0
  List<int> box4 = [0,3,0]; // 0
  List<int> box5 = [0,3,0,3,0]; // 3
  List<int> box6 = [5,0,3,0,6]; // 12
  List<int> box7 = [2, 1, 3]; // 1

  print(ca.checkCapacity(box1));
  print(ca.checkCapacity(box2));
  print(ca.checkCapacity(box3));
  print(ca.checkCapacity(box4));
  print(ca.checkCapacity(box5));
  print(ca.checkCapacity(box6));
  print(ca.checkCapacity(box7));
}
