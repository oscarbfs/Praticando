int checkCapacity(List<int> box) {
  int waterCapacity = 0;

  int maxRelief = box.reduce((value, element) => value > element ? value : element);
  List<int> boxCopy = [...box];

  int index = 0;

  while (index < maxRelief) {
    boxCopy = removerZerosDasExtremidades(boxCopy);

    List<int> zeros = boxCopy.where((elemento) => elemento == 0).toList();
    waterCapacity += zeros.length;

    for (int index = 0; index < boxCopy.length; index++) {
      if(boxCopy[index] > 0) boxCopy[index] -= 1;
    }

    index++;
  }

  return waterCapacity;
}

List<int> removerZerosDasExtremidades(List<int> lista) {
  int inicio = 0;
  while (inicio < lista.length && lista[inicio] == 0) {
    inicio++;
  }

  int fim = lista.length - 1;
  while (fim >= 0 && lista[fim] == 0) {
    fim--;
  }

  List<int> resultado = lista.sublist(inicio, fim + 1);

  return resultado;
}
