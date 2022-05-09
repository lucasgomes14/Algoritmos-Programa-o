#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(void)
{
 int tamanho,contador=0;
 scanf("%d", &tamanho);
 float lista[tamanho*tamanho],somador=0,matriz[tamanho][tamanho];
  for(int t=0;t<tamanho*tamanho;t++)
  {
    scanf("%f",&lista[t]);
  }
  for(int l=0;l<tamanho;l++)
  {
    for(int c=0;c<tamanho;c++)
    {
      matriz[l][c]=lista[contador];
      contador++;
    }
  }
  printf("tr(A) =");
  for(int i=0;i<tamanho;i++)
  {
    somador+=matriz[i][i];
    printf(" (%.2f)", matriz[i][i]);
    if(i!=tamanho-1)
    {
      printf(" +");
    }
    else
    {
      printf(" = %.2f", somador);
    }
  }
  return 0;
}