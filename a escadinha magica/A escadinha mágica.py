num=int(input())
m = 1
for c in range(1,num+1):
    for x in range(1, c+1):
        if x == 1:
            print(x,end=' ')
        else:
            print(x,end='')
        m+=1
    print()