#include <stdio.h>

int main(){
  int portugues, matematica, i=0, aprovados = 0;
  float redacao;

  while(i == 0){
    scanf("%d", &portugues);
    if(portugues < 0){
      i++;
    }
    else{
      scanf("%d", &matematica);
      scanf("%f", &redacao);
      if(portugues >=40 && matematica >=21 && redacao >= 7.0){
        aprovados++;
      }
    }
  }
  printf("%d",aprovados);
  return 0;
}