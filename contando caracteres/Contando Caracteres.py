anterior = 0
while True:
    texto = input()
    
    if texto == '0':
        break
    
    texto = texto.split()
    contagem_int = 0
    
    for i in range(len(texto)):
        contagem_int = int(len(texto[i]))
        if contagem_int >= anterior:
            maior = texto[i]
            anterior = contagem_int
        if i+1 == len(texto):
            print(contagem_int)
        else:
            print(contagem_int, end='-')
print('Maior palavra:',maior)