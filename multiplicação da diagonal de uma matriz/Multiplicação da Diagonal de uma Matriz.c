#include <stdio.h>

int main()
{
	int matriz[4][4],constante,linha=0,coluna=0,numero;
  scanf("%d",&constante);
  for(int i=0;i<17;i++)
  {
    if(i!=16)
    {
      scanf("%d",&matriz[coluna][linha]);
      coluna++;
      if(coluna==4)
      {
        coluna=0;
        linha++;
      }
    }
    else
    {
      scanf("%d",&numero);
    }
  }
  for(int l=0;l<4;l++)
    for(int c=0;c<4;c++)
    {
      if(l==c)
      {
        if(c!=3)
        {
          printf("%d ",matriz[l][c]*constante);
        }
        else
        {
          printf("%d \n",matriz[l][c]*constante);
        }
      }
      else
      {
        if(c!=3)
        {
          printf("%d ",matriz[l][c]);
        }
        else
        {
          printf("%d \n",matriz[l][c]);
        }
      }
    }
  return 0;
}