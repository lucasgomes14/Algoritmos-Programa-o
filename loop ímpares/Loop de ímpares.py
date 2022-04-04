n1=int(input())
n2=int(input())
c=0
while n1 <= n2:
    c= n1 % 2
    if c == 1:
        print(n1)
    n1+=1