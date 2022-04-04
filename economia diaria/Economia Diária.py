x = 0
c = 0
z = 0
for i in range(1,8):
    inicio=float(input())
    if inicio > (z+0.49):
        c+=1
    z=inicio
    x+=inicio
c-=1
print('R$ {:.2f}\n{}'.format(x,c))
