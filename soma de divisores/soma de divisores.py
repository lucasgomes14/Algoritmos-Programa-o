x=1
contador=0
acumulador=0
t=0
while x<=5:
    num=int(input())
    for c in range(1,num+1):
        if num%c==0:
            acumulador+=c
    if acumulador>t:
        contador=num
    t=acumulador
    acumulador=0
    x+=1
print(contador)