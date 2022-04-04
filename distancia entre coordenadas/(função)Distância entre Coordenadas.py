import math
#função
def raiz(xa,ya,xb,yb):
    print('{:.2f}'.format(math.sqrt(((xb-xa)**2)+((yb-ya)**2))))

#programa principal

quant = int(input())

for i in range(quant):
    inteiros = input().split()
    raiz(int(inteiros[0]),int(inteiros[1]),int(inteiros[2]),int(inteiros[3]))