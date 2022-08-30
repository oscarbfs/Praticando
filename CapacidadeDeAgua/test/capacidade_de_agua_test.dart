import 'package:capacidade_de_agua/capacidade_de_agua.dart';
import 'package:test/test.dart';

void main() {
  test(' teste 1: deve retornar 3 ', () {
    List listaRelevo = [3,0,3];

    expect(capacidadeDeAgua(listaRelevo), equals(3));
  });
  test(' teste 2: deve retornar 3 ', () {
    List listaRelevo = [3,0,4];

    expect(capacidadeDeAgua(listaRelevo), equals(3));
  });
  test(' teste 3: deve retornar 9', () {
    List listaRelevo = [4,0,3,0,4];

    expect(capacidadeDeAgua(listaRelevo), equals(9));
  });
  test(' teste 4: deve retornar 12', () {
    List listaRelevo = [4,0,3,0,4,0,3];

    expect(capacidadeDeAgua(listaRelevo), equals(9));
  });
}
