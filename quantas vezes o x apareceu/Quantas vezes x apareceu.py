lista = []
acumulador = 0

for i in range(10):
    num = int(input())
    lista.append(num)
x = int(input())

for i in lista:
    if i == x:
        acumulador+=1
print(acumulador)