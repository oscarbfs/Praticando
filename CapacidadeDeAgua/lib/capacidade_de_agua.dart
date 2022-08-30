int capacidadeDeAgua(List listaRelevo) {
  int capacidadeDeAgua = 0;
  int relevoMaisAlto = 0;

  // for (int index = 0; index < listaRelevo.length;index++) {
  //   if(relevo > relevoMaisAlto) {
  //     relevoMaisAlto = relevo;
  //   }
  // }

  // for(int index = 0; index <= listaRelevo.length - 1; index ++) {
  //   int atual = listaRelevo[index];
  //   if(!(index == 0) && (index == listaRelevo.length - 1)) {

  //     int anterior = listaRelevo[index - 1];  
  //     int seguinte = listaRelevo[index + 1];  
  //     int profundide = (seguinte - atual) + (atual - anterior);
  //     capacidadeDeAgua += (profundide < 0 ? 0 : profundide);

  //   } 
    //else if (index == listaRelevo.length - 1) {

    //   int anterior = listaRelevo[index - 1];  
    //   int profundide = atual - anterior;
    //   capacidadeDeAgua += (profundide < 0 ? 0 : profundide);

    // } else {

    //   int anterior = listaRelevo[index - 1];  
    //   int seguinte = listaRelevo[index + 1];  
    //   int profundide = (seguinte - atual) + (atual - anterior);
    //   capacidadeDeAgua += (profundide < 0 ? 0 : profundide);

    // }


  // }

  return capacidadeDeAgua;
}
