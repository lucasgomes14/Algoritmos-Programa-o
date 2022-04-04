def A (a):
    if a == 'a':
        return('@')

def E (e):
    if e == 'e':
        return('3')

def I (i):
    if i == 'i':
        return('1')
    
def O (o):
    if o == 'o':
        return('0')
    
def T (t):
    if t == 't':
        return('7')

def S (s):
    if s == 's':
        return('5')

palavras = input().lower()
lista = []
cont = 0
t = '00'

for i in range(len(palavras)):
    if palavras[i] == 'a':
        lista.append(A('a'))
        cont += 1
    elif palavras[i] == 'e':
        lista.append(E('e'))
        cont += 1
    elif palavras[i] == 'i':
        lista.append(I('i'))
        cont += 1
    elif palavras[i] == 'o':
        lista.append(O('o'))
        cont += 1
    elif palavras[i] == 't':
        lista.append(T('t'))
        cont += 1
    elif palavras[i] == 's':
        lista.append(S('s'))
        cont += 1
    elif palavras[i].isdigit():
        print('numeros\n0')
        break
    else:
        lista.append(palavras[i])
if i == len(palavras)-1:
    for i in range(len(lista)-1,-1,-1):
        if i == 0:
            print(lista[i])
        else:
            print(lista[i],end = '')
    print(cont)