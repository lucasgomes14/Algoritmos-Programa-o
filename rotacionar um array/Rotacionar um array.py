lista = []

quant = int(input())

for i in range(quant):
    lista.append(int(input()))

t = lista[-1]
deslocamento = int(input())
  
while lista[-1] == t:
    print(lista[deslocamento])
    del lista[deslocamento]

for i in range(len(lista)):
    print(lista[0])
    del lista[0]