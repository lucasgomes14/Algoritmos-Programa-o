v=0
while True:
    num=int(input())
    x=1*2
    if num == -1:
        break
    elif num == 0 or num == 1:
        print(1)
    elif num == 2:
        print(x)
    else:
        for c in range(3,num+1):
            v=x*c
            x=v
        print(v)