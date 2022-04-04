n = int(input())

coluna = []

for i in range(n):
    linha = []
    for c in range(n):
        linha.append(c+(i+1))
    coluna.append(linha)
    
for i in range(n-1):
    for c in range(i+1):
        coluna[i+1].pop(-1)
espaco = 2
for i in range(n):
    for c in range(len(coluna[i])):
        if c == len(coluna[i])-1:
            print(coluna[i][c])
            print(espaco*' ',end='')
            espaco+=2
        else:
            print(coluna[i][c],end=' ')
# for i in range(n):
#     for c in range(len(coluna[i])):
#         if c == len(coluna[i])-1:
#             print(coluna[i][c], '\n', espaco * ' ',end='')
#             espaco += 2
#         else:
#             print(coluna[i][c],end=' ')

