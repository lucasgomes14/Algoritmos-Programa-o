matriz = input().split()

for x in range(len(matriz)):
    matriz.append(int(matriz[x]))

matriz.pop(0)
matriz.pop(0)

coluna = []

for i in range(matriz[0]):
    linha = []
    for c in range(matriz[1]):
        elementos = int(input())
        linha.append(elementos)
    coluna.append(linha)
    
print('Matriz formada:')

contadormenor = 0
contadormaior = 0

for c in range(len(coluna)):
    for x in range(len(linha)):
        if x != len(linha)-1:
            print(coluna[c][x], end =' ')
        else:
            print(coluna[c][x], end = '')
        if coluna[c][x] < 0:
            contadormenor += 1
        elif coluna[c][x] > 0:
            contadormaior += 1
    print()

principal = 0
secundaria = 0

if matriz[0] == matriz[1]:
    for c in range(len(coluna)):
        principal += coluna[c][c]
    for x in range(len(coluna)-1,-1,-1):
        secundaria += coluna[x][x]
    print('A diagonal principal e secundaria tem valor(es) {} e {} respectivamente.'.format(principal, secundaria))
    
else:
    print('A diagonal principal e secundaria nao pode ser obtida.')

print('A matriz possui {} numero(s) menor(es) que zero.\nA matriz possui {} numero(s) maior(es) que zero.'.format(contadormenor, contadormaior))