while True:
    num=int(input())
    t1=0
    t2=1
    if num == 0:
        break
    elif num == 1:
        print(t1)
    else:
        for c in range(num):
            t3= t1+t2
            print('', t3,end='')
            t1=t2
            t2=t3
        print()
