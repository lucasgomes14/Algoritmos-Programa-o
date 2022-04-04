tamanho = int(input())

lista_str = []
lista_int = []
menor = 0
posicao = 0

lista_str = input().split(' ')
for x in range(tamanho):
    lista_int.append(int(lista_str[x]))

t = lista_int[0]

for i in lista_int:
    if i <= t:
        menor = i
    t = i
for c in range(tamanho):
    if lista_int[c] == menor:
        posicao = c
        
print('Menor valor: {}\nPosicao: {}'.format(menor, posicao))