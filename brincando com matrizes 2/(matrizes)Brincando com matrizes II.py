lista = []

for i in range(9):
    lista.append(int(input()))

coluna = []

somador = 0
divisor = 0
menor = lista[0]

for i in range(len(lista)):
    if lista[i] > 0:
        somador += lista[i]
        divisor += 1
    if lista[i] <= menor:
        menor = lista[i]
        if menor % 2 == 0:
            delta = 1
        else:
            delta = 0
            
for i in range(3):
    linha = []
    for c in range(3):
        linha.append(lista[c])
    for z in range(3):
        lista.pop(0)
    coluna.append(linha)
somadiagonal = 0
subtracao = 0

for i in range(3):
    for c in range(3):
        somadiagonal += coluna[i][c]

for i in range(3):
    subtracao += coluna[i][i]
    
print('{:.2f} {} {} {}'.format(somador/divisor,menor,delta,somadiagonal-subtracao))