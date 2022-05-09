#include <stdio.h>

int main(void) 
{
  int tamanho, l, c, somador = 0, contador = 0;
  scanf("%d", &tamanho);
  int matriz [tamanho][tamanho];
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
      if(l == 0)
      {
        if(c == 0)
        {
          if(matriz[l+1][c] >= 0)
          {
            somador += matriz[l+1][c];
            contador++;
          }
          if(matriz[l][c+1] >= 0)
          {
            somador += matriz[l][c+1];
            contador++;
          }
        }
        if(c == tamanho - 1)
        {
          if(matriz[l+1][c] >= 0)
          {
            somador += matriz[l+1][c];
            contador++;
          }
          if(matriz[l][c-1] >= 0)
          {
            somador += matriz[l][c-1];
            contador++;
          }
        }
        if(c != 0 && c != tamanho-1)
        {
          if(matriz[l][c-1] >= 0)
          {
            somador += matriz[l][c-1];
            contador++;
          }
          if(matriz[l][c+1] >= 0)
          {
            somador += matriz[l][c+1];
            contador++;
          }
          if(matriz[l+1][c] >= 0)
          {
            somador += matriz[l+1][c];
            contador++;
          }
        }
      }
      if(l == tamanho - 1)
      {
        if(c == 0)
        {
          if(matriz[l-1][c] >= 0)
          {
            somador += matriz[l-1][c];
            contador++;
          }
          if(matriz[l][c+1] >= 0)
          {
            somador += matriz[l][c+1];
            contador++;
          }
        }
        if(c == tamanho - 1)
        {
          if(matriz[l-1][c] >= 0)
          {
            somador += matriz[l-1][c];
            contador++;
          }
          if(matriz[l][c-1] >= 0)
          {
            somador += matriz[l][c-1];
            contador++;
          }
        }
        if(c != 0 && c != tamanho-1)
        {
          if(matriz[l][c-1] >= 0)
          {
            somador += matriz[l][c-1];
            contador++;
          }
          if(matriz[l][c+1] >= 0)
          {
            somador += matriz[l][c+1];
            contador++;
          }
          if(matriz[l-1][c] >= 0)
          {
            somador += matriz[l-1][c];
            contador++;         
          }
        }
      }
      if(c == 0 && l != 0 && l != tamanho-1)
      {
        if(matriz[l-1][c] >= 0)
        {
          somador += matriz[l-1][c];
          contador++;
        }
        if(matriz[l+1][c] >= 0)
        {
          somador += matriz[l+1][c];
          contador++;
        }
        if(matriz[l][c+1] >= 0)
        {
          somador += matriz[l][c+1];
          contador++;
        }
      }
      if(c == tamanho-1 && l != 0 && l != tamanho-1)
      {
        if(matriz[l-1][c] >= 0)
        {
          somador += matriz[l-1][c];
          contador++;
        }
        if(matriz[l+1][c] >= 0)
        {
          somador += matriz[l+1][c];
          contador++;
        }
        if(matriz[l][c-1] >= 0)
        {
          somador += matriz[l][c-1];
          contador++;
        }
      }
      if(l != 0 && l != tamanho -1 && c != 0 && c != tamanho -1)
      {
        if(matriz[l+1][c] >= 0)
        {
          somador += matriz[l+1][c];
          contador++;
        }
        if(matriz[l-1][c] >= 0)
        {
          somador += matriz[l-1][c];
          contador++;
        }
        if(matriz[l][c-1] >= 0)
        {
          somador += matriz[l][c-1];
          contador ++;
        }
        if(matriz[l][c+1] >= 0)
        {
          somador += matriz[l][c+1];
          contador ++;
        }
      }
    }
  }
  printf("%d\n%d",contador, somador);
  return 0;
}