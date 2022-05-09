#include <stdio.h>

int main(){
	float valor, resultado = 0, resultado2;
	int divisivel = 0;
	printf("Insira os valores das doacoes:\n");
	while(scanf("%f",&valor), valor > 0){
		resultado += valor;
		divisivel ++;
	}
	if (divisivel == 0){
	    resultado2 = 0.00;
	}else{
	    resultado2 = resultado / divisivel;
	}
	printf("Total arrecadado: %.2f\n", resultado);
	printf("Valor medio da doacao: %.2f\n",resultado2);
	return 0;
}