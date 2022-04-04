numero = int(input())

coluna = []
somatorio = 0

for i in range(numero):
    linha = []
    for c in range(numero):
        somatorio +=1
        linha.append(somatorio)
    coluna.append(linha)
    
principal = []

for i in range(numero):
    principal.append(coluna[i][i])

secundaria = []
teste = numero-1

for c in range(numero):
    secundaria.append(coluna[c][teste])
    teste -= 1

print('Matriz:')

for i in range(numero):
    for c in range(numero):
        if c == numero -1:
            print(' ', coluna[i][c], end ='')
        else:
            print(' ',coluna[i][c], end = '')
    print()

print('Diagonal Principal:\n')
espacos = 1
for i in range(numero):
    print(espacos * ' ',principal[i])

print('Diagonal Secundaria:\n')
espacos = 1
for i in range(numero):
    print(espacos * ' ',secundaria[i])
