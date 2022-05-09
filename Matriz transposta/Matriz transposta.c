#include <stdio.h>

int main()
{
  int linha,coluna;
  scanf("%d %d",&linha,&coluna);
  int matriz[linha][coluna];
  for(int l=0;l<linha;l++)
  {
    for(int c=0;c<coluna;c++)
    {
      scanf("%d",&matriz[l][c]);
    }
  }

  for(int l=0;l<coluna;l++)
  {
    for(int c=0;c<linha;c++)
    {
      if(c!=linha-1)
      {
        printf("%d ",matriz[c][l]);
      }
      else
      {
        printf("%d \n",matriz[c][l]);
      }
    }
  }
  return 0;
}