num1=int(input())
num2=int(input())
x = 0
if num1 < num2:
    for i in range(num1,num2+1):
        if i >= 0:
            x+= i
else:
    for i in range(num2,num1+1):
        if i >= 0:
            x+= i
print(x)
        