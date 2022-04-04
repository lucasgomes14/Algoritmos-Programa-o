#função


def cripto(letra):
    if letra == 'a' or  letra == 'e' or letra == 'i' or  letra == 'o' or\
        letra == 't' or  letra == 's':
        if letra == 'a':
            return '@'
        elif letra == 'e':
            return '3'
        elif letra == 'i':
            return '1'
        elif letra == 'o':
            return '0'
        elif letra == 't':
            return '7'
        else:
            return '5'
    else:
        return letra
        
#programa principal

lista = list(input().lower())
inverso = []
cont = 0
for i in range(len(lista)-1,-1,-1):
    inverso.append(lista[i])
    
for i in range(len(inverso)):
    if inverso[i] == 'a' or  inverso[i] == 'e' or inverso[i] == 'i' or  inverso[i] == 'o' or\
        inverso[i] == 't' or  inverso[i] == 's':
            cont += 1
    if inverso[i].isdigit():
        print('numeros\n0')
        break
    elif i == len(inverso)-1:
        for x in range(len(inverso)):
            if len(inverso)-1 == x:
                print(cripto(inverso[x]))
                print(cont)
            else:
                print(cripto(inverso[x]),end = '')
    else:
        continue