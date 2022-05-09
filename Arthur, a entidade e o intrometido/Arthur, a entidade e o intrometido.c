#include <stdio.h>

int main(void) 
{
  int tamanho, l, c, soma_arthur = 0, soma_entidade = 0, soma_intrometido = 0;
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
      if(l % 2 == 0)
      {
        soma_arthur += matriz[l][c];
      }
      if(c % 2 != 0)
      {
        soma_entidade += matriz[l][c];
      }
      if(l == c)
      {
        soma_intrometido += matriz[l][c];
      }
    }
  }
  if(soma_arthur > soma_entidade && soma_arthur > soma_intrometido)
  {
    printf("Arthur venceu!\nResultado: %d", soma_arthur);
  }
  else if(soma_entidade > soma_arthur && soma_entidade > soma_intrometido)
  {
    printf("A entidade venceu!\nResultado: %d", soma_entidade);
  }
  else if(soma_intrometido > soma_arthur && soma_intrometido > soma_entidade)
  {
    printf("O intrometido venceu!\nResultado: %d", soma_intrometido);
  }
  else
  {
    if(soma_arthur == soma_entidade && soma_arthur == soma_intrometido)
    {
      printf("Empate!\nResultado: %d", soma_arthur);
    }
    else if(soma_arthur == soma_entidade)
    {
      printf("Empate!\nResultado: %d", soma_arthur);
    }
    else if(soma_arthur == soma_intrometido)
    {
      printf("Empate!\nResultado: %d", soma_arthur);
    }
    else if(soma_entidade == soma_intrometido)
    {
      printf("Empate!\nResultado: %d", soma_entidade);
    }
  }
  return 0;
}