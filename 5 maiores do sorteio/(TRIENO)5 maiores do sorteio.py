quant = input().split()

lista_de_numeros = []

for i in range(int(quant[0])):
    num = input()
    lista_de_numeros.append(num)

resultado_str = []

for i in range(int(quant[0])):
    if lista_de_numeros[i][-1] == quant[-1]:
        resultado_str.append(lista_de_numeros[i])

resultado_int = []

for i in range(int(len(resultado_str))):
    resultado_int.append(int(resultado_str[i]))

while len(resultado_str) < 5:
    resultado_int.append(-1)
    resultado_str.append('-1')

resultado_int.sort()

for i in range(5):
    print(resultado_int[i])