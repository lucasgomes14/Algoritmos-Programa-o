#include <stdio.h>

int main(void) 
{
  int tamanho, l, c;
  char booleano; 
  scanf("%d", &tamanho);
  int matriz [tamanho][tamanho], t = tamanho;
  for(l = 0;l < tamanho;l++)
  {
    for(c = 0;c < tamanho;c++)
    {
      scanf("%d", &matriz[l][c]);
    }
  }
  for(l = 0;l < tamanho;l++)
  {
    for(c = 0;c < tamanho;c++)
    {
      if(c == tamanho-1)
      {
        printf("%d \n", matriz[l][c]);
      }
      else
      {
        printf("%d ", matriz[l][c]);
      }
    }
  }
  
  int li = 0, co = 0, v[t], n = 0;
  while(li < tamanho)
  {

    if(matriz[li][co] != 0 && matriz[li][co] != 1)
    {
      printf("False");
      break;
    }
    if(matriz[li][co] == 0)
    {
      n++;
    }
    if(co == tamanho -1 && n!= tamanho - 1)
    {
      printf("False");
      break;
    }
    if(matriz[li][co] == 1)
    {
      if(v[co] == 1)
      {
        printf("False");
        break;
      }
      else
      {
        v[co] = 1;
      }
    }
    if(li == tamanho - 1 && co == tamanho - 1)
    {
      printf("True");
    }
    co ++;
    if(co == tamanho)
    {
      co = 0;
      li++;
      n = 0;
    }
  }
  return 0;
}