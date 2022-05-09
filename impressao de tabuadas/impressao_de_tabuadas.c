#include <stdio.h>
int main(){
	int valor1,valor2;
	while(1){
		scanf("%d",&valor1);
		if(valor1 < 1 || valor1 > 9 ){
			printf("Insira um n�mero inicial entre 1 e 9\n");
			continue;
		}else{
			break;
		}
	}
	while(1){
		scanf("%d",&valor2);
		if(valor2 < 1 || valor2 > 9){
			printf("Insira um n�mero final entre 1 e 9\n");
			continue;
		}if(valor2 < valor1){
			printf("Nenhuma tabuada nesse intervalo\n");
			break;
		}else{
			for(int i = valor1; i <= valor2; i++){
				for(int x = 1; x <= 9; x++){
					printf("%d x %d = %d\n", i, x,(i*x));
				}printf("\n");
			}
	
			break;
		}
	}
	return 0;
}