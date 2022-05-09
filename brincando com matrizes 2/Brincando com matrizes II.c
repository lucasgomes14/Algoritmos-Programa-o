#include <stdio.h>

int main()
{
  int matriz[3][3],linha=0,coluna=0,divisor=0,delta,soma=0;
  float somapositivos=0;
  for(int i=0;i<9;i++)
  {
    scanf("%d",&matriz[linha][coluna]);
    coluna++;
    if(coluna==3)
    {
      coluna=0;
      linha++;
    }
  }
  int menor=matriz[0][0];
  for(int l=0;l<3;l++)
    for(int c=0;c<3;c++)
    {
      if(l!=c)
      {
        soma+=matriz[l][c];
      }
      if(matriz[l][c]>0)
      {
        divisor++;
        somapositivos+= (float)matriz[l][c];
      }
      if(matriz[l][c]<menor)
      {
        menor=matriz[l][c];
      }
    }
  if(menor%2==0)
  {
    delta=1;
  }
  else
  {
    delta=0;
  }
  printf("%.2f %d %d %d",(somapositivos/divisor),menor,delta,soma);
  return 0;
}