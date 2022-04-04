lista_str = []
lista_int = []
contador = 0

quant = int(input())

for i in range(quant):
    lista_str = input().split(' ')
    for c in range(len(lista_str)):
        lista_int.append(int(lista_str[c]))
    if lista_int[0] > lista_int[1]:
        contador += lista_int[1]
    lista_int.pop()
    lista_int.pop()
print(contador)