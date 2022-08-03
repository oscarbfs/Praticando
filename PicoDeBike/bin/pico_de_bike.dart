import 'package:pico_de_bike/data/locacao_data.dart';
import 'package:pico_de_bike/pico_de_bike.dart';
void main(List<String> args) {
  List<Locacao> listLocacao = [
    Locacao(horarioEntrada: 1, horarioSaida: 3, quantidade: 2),
    Locacao(horarioEntrada: 2, horarioSaida: 4, quantidade: 2),
    Locacao(horarioEntrada: 4, horarioSaida: 5, quantidade: 1),
  ];

  print("${picoLocacao(listLocacao)}\n");

  List<Locacao> listLocacao1 = [
    Locacao(horarioEntrada: 1, horarioSaida: 4, quantidade: 2),
    Locacao(horarioEntrada: 2, horarioSaida: 3, quantidade: 2),
    Locacao(horarioEntrada: 4, horarioSaida: 5, quantidade: 1),
  ];
  print("${picoLocacao(listLocacao1)}\n");

  List<Locacao> listLocacao2 = [
    Locacao(horarioEntrada: 2, horarioSaida: 4, quantidade: 3),
    Locacao(horarioEntrada: 4, horarioSaida: 5, quantidade: 2),
    Locacao(horarioEntrada: 5, horarioSaida: 6, quantidade: 1),
  ];
  print("${picoLocacao(listLocacao2)}\n");

  List<Locacao> listLocacao3 = [
    Locacao(horarioEntrada: 2, horarioSaida: 4, quantidade: 2),
    Locacao(horarioEntrada: 4, horarioSaida: 5, quantidade: 3),
    Locacao(horarioEntrada: 5, horarioSaida: 6, quantidade: 1),
  ];
  print("${picoLocacao(listLocacao3)}\n");
}

