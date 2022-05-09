#include <stdio.h>

int main(){
  int quantidade, deslocamento;
  scanf("%d", &quantidade);
  int vetor[quantidade];
  for(int i = 0; i < quantidade; i++){
    scanf("%d", &vetor[i]);
  }
  scanf("%d", &deslocamento);
  for(int i = (quantidade-deslocamento); i < quantidade; i++){
    printf("%d\n", vetor[i]);
  }for(int i = 0; i < (quantidade - deslocamento); i++){
    printf("%d\n", vetor[i]);
  }return 0;
}