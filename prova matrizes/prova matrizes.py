n = int(input())
m1 = []
m2 = []
lista = []
for c in range(n):
    m1.append(input().split())
for c in range(n):
    m2.append(input().split())

sinal=input()

if sinal == '+-':
    for i in range(n):
        for c in range(n):
            if (i+1) % 2 == 1 and c == n-1:
                print('{:.2f}'.format(float(m1[i][c])+float(m2[i][c])))
            elif (i+1) % 2 == 1:
                print('{:.2f}'.format(float(m1[i][c])+float(m2[i][c])), end = ' ')
            elif (i+1) % 2 == 0 and c == n-1:
                print('{:.2f}'.format(float(m1[i][c])-float(m2[i][c])))
            else:
                print('{:.2f}'.format(float(m1[i][c])-float(m2[i][c])), end = ' ')
else:
    for i in range(n):
        for c in range(n):
            if (i+1) % 2 == 0 and c == n-1:
                print('{:.2f}'.format(float(m1[i][c])+float(m2[i][c])))
            elif (i+1) % 2 == 0:
                print('{:.2f}'.format(float(m1[i][c])+float(m2[i][c])), end = ' ')
            elif (i+1) % 2 == 1 and c == n-1:
                print('{:.2f}'.format(float(m1[i][c])-float(m2[i][c])))
            else:
                print('{:.2f}'.format(float(m1[i][c])-float(m2[i][c])), end = ' ')