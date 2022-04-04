lista = []
contador = 0

numero = input()

lista = input().split(' ')

for i in range(len(lista)):
    if lista[i] == numero:
        contador += 1

print(contador)