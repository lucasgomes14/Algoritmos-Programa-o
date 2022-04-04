lista = []

for i in range(3):
    num = int(input())
    lista.append(num)
    
if lista[0] > lista[1] and lista[1] > lista[2]:
    print(lista[1])

elif lista[1] > lista[0] and lista[0] > lista[2]:
    print(lista[0])

else:
    print(lista[2])