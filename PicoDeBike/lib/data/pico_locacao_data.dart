import 'package:equatable/equatable.dart';

class PicoLocacao extends Equatable {
  int horarioComeco;
  int horarioFim;
  int quantidade;

  PicoLocacao({
    required this.horarioComeco,
    required this.horarioFim,
    required this.quantidade,
  });

  @override
  String toString() {
    return "Horário de começo: $horarioComeco\nHorário de termino: $horarioFim\nQuantidade de Locações: $quantidade";
  }

  @override
  List<Object?> get props => [
        horarioComeco,
        horarioFim,
        quantidade,
      ];
}
