num=int(input())
a=0
b=1
c=2
d=0
if num <= 0:
    print('Falso')
else:
    while d<num:
        a+=1
        b+=1
        c+=1
        d=a*b*c
        if a+1==b and b+1==c and d==num:
            break
    if d == num:
        print('{} * {} * {} = {}\nVerdadeiro'.format(a,b,c,num))
    else:
        print('Falso')
