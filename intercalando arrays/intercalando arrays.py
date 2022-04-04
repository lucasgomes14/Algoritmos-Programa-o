lista1 = []
lista2 = []

tamanho = int(input())

for i in range(tamanho):
    numero = int(input())
    lista1.append(numero)

for c in range(tamanho):
    numero2 = int(input())
    lista2.append(numero2)

for x in range(tamanho):
    print(lista1[x])
    print(lista2[x])