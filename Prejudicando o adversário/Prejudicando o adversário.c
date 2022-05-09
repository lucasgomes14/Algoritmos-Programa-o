#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(void)
{
  int tamanho;

  scanf("%d",&tamanho);
  int matriz[tamanho][tamanho];
  for(int l=0;l<tamanho;l++)
  {
    for(int c=0;c<tamanho;c++)
    {
      scanf("%d", &matriz[c][l]);
    }
  }
  for(int l=0;l<tamanho;l++)
  {
    for(int c=0;c<tamanho;c++)
    {
      if(matriz[l][c]<0)
      {
        if(c==tamanho-1)
        {
          printf("%d\n",matriz[l][c]*2);
        }
        else
        {
          printf("%d ",matriz[l][c]*2);
        }
      }
      else
      {
        if(c==tamanho-1)
        {
          printf("%d\n",matriz[l][c]);
        }
        else
        {
          printf("%d ",matriz[l][c]);
        }
      }
    }
  }
  return 0;
}