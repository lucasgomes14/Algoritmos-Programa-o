x= 0
count= 0
while True:
    n=int(input())
    if n == -1:
        break
    elif x == n:
        count+=1
    x+=1
print(count)