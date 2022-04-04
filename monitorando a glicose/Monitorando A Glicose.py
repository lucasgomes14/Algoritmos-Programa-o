contador=0
acumulador=0
while True:
    glicose=int(input())
    if glicose == 0:
        break
    else:
        acumulador+=glicose
        contador+=1
if contador != 0:
    media=acumulador/contador
    if media < 110:
        print('Glicose Normal')
    elif media >= 200:
        print('Glicose Muito Alta')
    else:
        print('Glicose Alterada')