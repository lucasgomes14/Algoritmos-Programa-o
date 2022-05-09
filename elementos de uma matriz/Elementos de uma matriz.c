#include <stdio.h>

int main()
{
  int linha, coluna,l=0,c=0,somaprincipal=0,somasecundaria=0,maiorque0=0,menorque0=0;
  scanf("%d %d", &linha,&coluna);
  int matriz[linha][coluna],lsecundaria=0,csecundaria=coluna-1;
  for(int i=0;i<(linha*coluna);i++)
  {
    scanf("%d",&matriz[l][c]);
    c++;
    if(c==coluna)
    {
      c=0;
      l++;
    }
  }

  printf("Matriz formada:\n");
  for(int l=0;l<linha;l++)
    for(int c=0;c<coluna;c++)
    {
      if(matriz[l][c]>0)
      {
        maiorque0++;
      }
      if(matriz[l][c]<0)
      {
        menorque0++;
      }
      if(c!=coluna-1)
      {
        printf("%d ",matriz[l][c]);
      }
      else
      {
        printf("%d\n",matriz[l][c]);
      }
      if(l==c)
      {
        somaprincipal+=matriz[l][c];
      }
      if(l==lsecundaria && c==csecundaria)
      {
        somasecundaria+=matriz[l][c];
        lsecundaria++;
        csecundaria--;
      }
    }
  if(linha==coluna)
  {
    printf("A diagonal principal e secundaria tem valor(es) %d e %d respectivamente.\n",somaprincipal,somasecundaria);
  }
  else
  {
    printf("A diagonal principal e secundaria nao pode ser obtida.\n");
  }
  printf("A matriz possui %d numero(s) menor(es) que zero.\n",menorque0);
  printf("A matriz possui %d numero(s) maior(es) que zero.\n",maiorque0);
  return 0;
}