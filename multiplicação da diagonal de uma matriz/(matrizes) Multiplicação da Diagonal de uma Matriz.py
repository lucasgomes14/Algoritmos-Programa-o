k = int(input())
lista = []
while True:
    num = int(input())
    if num == 0:
        break
    else:
        lista.append(num)
contagem = len(lista)//4
colunas = []
for c in range(4):
    matriz = []
    for i in range(c,16,contagem):
        matriz.append(lista[i])
    colunas.append(matriz)

for i in range(4):
    colunas[i][i] = colunas[i][i] * k

for c in range(4):
    for i in range(4):
        if i == 3:
            print(colunas[c][i],'')
        else:
            print(colunas[c][i], end = ' ')