import 'package:capacidade_de_agua/capacidade_de_agua.dart';
import 'package:test/test.dart';

void main() {
  test(' teste 1: deve retornar 3 ', () {
    List<int> box = [3,0,3];

    expect(checkCapacity(box), equals(3));
  });
  test(' teste 2: deve retornar 0 ', () {
    List<int> box = [0,0,3];

    expect(checkCapacity(box), equals(0));
  });
  test(' teste 3: deve retornar 0', () {
    List<int> box = [3,0,0];

    expect(checkCapacity(box), equals(0));
  });
  test(' teste 4: deve retornar 0', () {
    List<int> box = [0,3,0];

    expect(checkCapacity(box), equals(0));
  });
  test(' teste 4: deve retornar 3', () {
    List<int> box = [0,3,0,3,0];

    expect(checkCapacity(box), equals(3));
  });
  test(' teste 4: deve retornar 12', () {
    List<int> box = [5,0,3,0,6];

    expect(checkCapacity(box), equals(12));
  });
  test(' teste 4: deve retornar 1', () {
    List<int> box = [2, 1, 3];

    expect(checkCapacity(box), equals(1));
  });
}
