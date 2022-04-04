lista1 = []
lista2 = []
lista3 = []

quantDaPrimeira = int(input())
if quantDaPrimeira == 0:
        print('Erro - A lista deve ter pelo menos 1 elemento.')
else:        
    for i in range(quantDaPrimeira):
        lista1.append(int(input()))
    
    quantDaSegunda = int(input())
        
    if quantDaSegunda == 0:
        print('Erro - A lista deve ter pelo menos 1 elemento.')
    else:
        for c in range(quantDaSegunda):
            lista2.append(int(input()))
                
        lista3 = lista1 + lista2

        for i in lista3:
            print('', str(i), end='')
