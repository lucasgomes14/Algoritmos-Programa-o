contador1 = 0
contador2 = 0
num1 = 0
num = 0
while num != 999:
    num=int(input())
    num1= num
    if num > 2 and num != 999:
        contador2+= 1
        contador1+=((num1-2)*12.89)
    num1 = 0

print('{:.2f}\n{}'.format(contador1, contador2))