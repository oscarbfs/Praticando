import 'data/locacao_data.dart';
import 'data/pico_locacao_data.dart';

PicoLocacao picoLocacao(List<Locacao> listLocacao) {
  PicoLocacao picoLocacao =
      PicoLocacao(horarioComeco: 0, horarioFim: 0, quantidade: 0);

  Map<int, int> quantidadePorHora = {};

  List<int> horasComMaiorQuantidade = [];

  int maiorQuantidade = 0;

  for (Locacao locacao in listLocacao) {
    for (int hora = locacao.horarioEntrada; hora < locacao.horarioSaida; hora++) {
      quantidadePorHora[hora] = (quantidadePorHora[hora] ?? 0) + locacao.quantidade;
      if (quantidadePorHora[hora]! > maiorQuantidade) {
        maiorQuantidade = quantidadePorHora[hora]!;
      }
    }
  }

  for (int hora in quantidadePorHora.keys) {
    if (quantidadePorHora[hora] == maiorQuantidade) {
      horasComMaiorQuantidade.add(hora);
    }
  }

  picoLocacao.horarioComeco = horasComMaiorQuantidade[0];
  picoLocacao.horarioFim =
      horasComMaiorQuantidade[horasComMaiorQuantidade.length - 1] + 1;
  picoLocacao.quantidade = maiorQuantidade;

  return picoLocacao;
}

