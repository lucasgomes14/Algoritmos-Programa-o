#include <stdio.h>

int main(){
  int numero,acumulador = 0, contador = 0, resultado, i, x;

  for (i = 0; i < 5; i++){
    scanf("%d", &numero);
    for(x = 1; x <= numero; x++){
      if(x % numero == 0){
        acumulador+= x;
      }
    }
    if (acumulador > contador){
      resultado = numero;
    }
    contador = acumulador;
    acumulador = 0;
  }
  printf("%d", resultado);
  return 0;
}