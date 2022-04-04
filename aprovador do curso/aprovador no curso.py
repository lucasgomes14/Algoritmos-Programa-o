contador=0
while True:
    port=int(input())
    if port < 0:
        break
    else:
        mat=int(input())
        red=float(input())
    
    if port >= 40 and mat >= 21 and red >= 7:
        contador+=1
print(contador)