def quadrado(baseealtura):
    return(baseealtura**2)

def retangulo(b,h):
    return(b*h)

def circulo(r):
    return(3.14*(r**2))

def percentual(a,b):
    return((a*100)/b)

def resumo(circulo,retangulo,quadrado,quant,percentual):
    print('Maior circulo: {:.2f}'.format(circulo))
    print('Maior retangulo: {:.2f}'.format(retangulo))
    print('Maior quadrado: {:.2f}'.format(quadrado))
    print('Quantidade de figuras {}'.format(quant))
    print('Percentual de circulos: {:.2f}'.format(percentual))
    
maior_quadrado = 0
maior_retangulo = 0
maior_circulo = 0
repeticao = 0
circulos = 0

while True:
    forma = input().lower()
    if forma == 'sair':
        break
    elif forma == 'q':
        baseealtura = int(input())
        var = quadrado(baseealtura)
        if baseealtura < 0:
            maior_quadrado = -1
        elif var > maior_quadrado:
            maior_quadrado = var
        
    elif forma == 'r':
        base = int(input())
        altura = int(input())
        var = retangulo(base,altura)
        if base < 0:
            maior_retangulo = -1
        elif var > maior_retangulo:
            maior_retangulo = var
            
    else:
        raio = int(input())
        circulos += 1
        var = circulo(raio)
        if raio < 0:
            maior_circulo = -1
        elif var > maior_circulo:
            maior_circulo = var
            
    repeticao += 1
    
percentual = percentual(circulos,repeticao)

resumo(maior_circulo,maior_retangulo,maior_quadrado,repeticao,percentual)