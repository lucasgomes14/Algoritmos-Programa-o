#include <stdio.h>

float porcentagem(float a,float b){
  return a * 0.15 + b;
}

int main(){
  char nome[10];
  float salario_fixo,vendas,resultado;
  scanf("%s", &nome);
  scanf("%f", &salario_fixo);
  scanf("%f", &vendas);
  resultado = porcentagem(vendas, salario_fixo);
  printf("TOTAL = R$ %.2f", resultado);
  return 0;
}