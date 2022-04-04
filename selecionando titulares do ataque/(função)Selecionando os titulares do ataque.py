def desempenho (x):
    return(2*x)
    
def gols (x):
    return(3.5*x)

def cansaco (x):
    return(1.5*x)

def entrosamento (x):
    return(2*x)


melhores = []

contador = 1

while True:
    if contador == 6:
        break
    else:
        zeros = 0
        nome = input()
        desempenhovar = int(input())
        golsvar = int(input())
        cansacovar = int(input())
        entrosamentovar = int(input())
        
        if desempenhovar == 0:
            zeros +=1
        if golsvar == 0:
            zeros +=1
        if cansacovar == 0:
            zeros +=1
        if entrosamentovar == 0:
            zeros +=1
        
        if zeros >= 2:
            caracteristicas = 0
            melhores.append(caracteristicas)
        else:
            caracteristicas = desempenho(desempenhovar)+gols(golsvar)+cansaco(cansacovar)+entrosamento(entrosamentovar)
            melhores.append(caracteristicas)
    contador += 1

melhores.sort()

print(melhores[-1])
print(melhores[-2])
print(melhores[-3])