#include <stdio.h>

int main(void) {
  int quantidade, contador = 0, numero;
  while(1){
    scanf("%d", &quantidade);
    if(quantidade < 2 || quantidade > 12){
      printf("Informe um valor entre 2 e 12!\n");
    }
    else{
      break;
    }
  }
  while(contador < quantidade){
    scanf("%d", &numero);
    int acumulador = 0;
    for(int i = 1; i <= numero; i++){
      if(numero % i == 0){
        acumulador++;
      }
    }if(acumulador == 2){
      printf("%d ", numero);
      contador ++;
    }
  }
}
