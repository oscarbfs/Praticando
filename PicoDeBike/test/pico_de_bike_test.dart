import 'package:pico_de_bike/data/locacao_data.dart';
import 'package:pico_de_bike/data/pico_locacao_data.dart';
import 'package:pico_de_bike/pico_de_bike.dart';
import 'package:test/test.dart';

void main() {
  test(' teste 1: deve retornar 2 a 3, 4 bikes ', () {
      List<Locacao> listLocacao = [
    Locacao(horarioEntrada: 1, horarioSaida: 3, quantidade: 2),
    Locacao(horarioEntrada: 2, horarioSaida: 4, quantidade: 2),
    Locacao(horarioEntrada: 4, horarioSaida: 5, quantidade: 1),
  ];

    expect(picoLocacao(listLocacao), equals(PicoLocacao(horarioComeco: 2, horarioFim: 3, quantidade: 4,)));
  });
  test(' teste 2: deve retornar 2 a 3, 4 bikes ', () {
      List<Locacao> listLocacao1 = [
    Locacao(horarioEntrada: 1, horarioSaida: 4, quantidade: 2),
    Locacao(horarioEntrada: 2, horarioSaida: 3, quantidade: 2),
    Locacao(horarioEntrada: 4, horarioSaida: 5, quantidade: 1),
  ];

    expect(picoLocacao(listLocacao1), equals(PicoLocacao(horarioComeco: 2, horarioFim: 3, quantidade: 4,)));
  });
  test(' teste 3: deve retornar 2 a 4, 3 bikes ', () {
      List<Locacao> listLocacao2 = [
    Locacao(horarioEntrada: 2, horarioSaida: 4, quantidade: 3),
    Locacao(horarioEntrada: 4, horarioSaida: 5, quantidade: 2),
    Locacao(horarioEntrada: 5, horarioSaida: 6, quantidade: 1),
  ];

    expect(picoLocacao(listLocacao2), equals(PicoLocacao(horarioComeco: 2, horarioFim: 4, quantidade: 3,)));
  });
  test(' teste 4: deve retornar 4 a 5, 3 bikes ', () {
      List<Locacao> listLocacao3 = [
    Locacao(horarioEntrada: 2, horarioSaida: 4, quantidade: 2),
    Locacao(horarioEntrada: 4, horarioSaida: 5, quantidade: 3),
    Locacao(horarioEntrada: 5, horarioSaida: 6, quantidade: 1),
  ];

    expect(picoLocacao(listLocacao3), equals(PicoLocacao(horarioComeco: 4, horarioFim: 5, quantidade: 3,)));
  });
}
