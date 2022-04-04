acumulador=0
maior=0

valortotal=float(input())
quantfuncionarios=int(input())

for c in range(quantfuncionarios):
    nome=input()
    valorpago=float(input())
    if valorpago>maior:
        nomemaior=nome
        valormaior=valorpago
    maior=valorpago
    acumulador+=valorpago
resultado=acumulador-valortotal
if acumulador>valortotal:
    print('{} pagou R$ {:.1f}\nValor excedente: sobra R$ {:.1f}'.format(nomemaior,valormaior,resultado))
else:
    print('{} pagou R$ {:.1f}\nValor insuficiente: falta R$ {:.1f}'.format(nomemaior,valormaior,resultado*-1))
