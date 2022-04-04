n = int(input())

coluna = []

for i in range(n):
    for c in range(1):
        numeros = input().split()
        for x in range(len(numeros)):
            numeros.append(float(numeros[x]))
        for z in range(n):
            numeros.pop(0)
    coluna.append(numeros)

somatorio = 0
teste = 'tr(A) ='
for i in range(len(coluna)):
    somatorio += coluna[i][i]
    if i == len(coluna)-1:
        teste += (' ({:.2f}) ='.format(coluna[i][i]))
    else:
        teste += (' ({:.2f}) +'.format(coluna[i][i]))
        
print('{} {:.2f}'.format(teste,somatorio))
