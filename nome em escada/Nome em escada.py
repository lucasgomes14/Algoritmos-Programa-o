nome = input()

for i in range(len(nome)):
    for c in range(i+1):
        print(nome[c].upper(), end='')
    print()