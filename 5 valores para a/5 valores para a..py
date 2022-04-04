contador=0
for x in range(5):
    num=float(input('Digite um valor: '))
    if num < 0:
        contador+=1
print('Foram digitados {} numeros negativos'.format(contador))