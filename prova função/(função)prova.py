#função
def divisivel(x):
    if x % 3 == 0:
        return True

def fatorial(x):
    cont = 1
    if x < 2:
        return 1
    else:
        for i in range(2,x+1):
            cont*= i
        return cont

def s(x):
    cont = 0
    for i in range(x+1):
        t = fatorial(i)
        cont += x/t
    return cont


#programa principal
contador = 0
for i in range(5):
    num = int(input())
    if num > -1:
        if divisivel(num) == True:
            contador += fatorial(num)
        else:
            contador += s(num)
    else:
        continue
print('{:.2f}'.format(contador))