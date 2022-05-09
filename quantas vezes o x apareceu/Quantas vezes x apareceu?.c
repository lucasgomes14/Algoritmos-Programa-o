#include <stdio.h>
int main(){
	int lista[10], numero, contador = 0;
	for(int i= 0;i<10;i++){
		scanf("%d",&lista[i]);
	}
	scanf("%d", &numero);
	for(int i = 0;i<10; i++){
		if(lista[i] == numero){
			contador ++;
		}
	}
	printf("%d", contador);
	return 0;
}