num=int(input())
a=0
b=0
while True:
    if num == 0:
        break
    a+=1
    b+=1
    a1=a*a
    b1=b*b
    if a1-b1==num:
        print('{} - {}'.format(a,b))