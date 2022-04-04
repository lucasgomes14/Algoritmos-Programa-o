quant = int(input())

lista = []
somatorio = 0
acumuladoracima = 0
acumuladorabaixo = 0

for i in range(quant):
    nota = int(input())
    lista.append(nota)
    somatorio += nota
    
media = somatorio / quant

acima = media + media * 0.1

abaixo= media - media * 0.1

for i in lista:
    if i > acima:
        acumuladoracima += 1
    if i < abaixo:
        acumuladorabaixo += 1

print('{:.2f}\n{}\n{}'.format(media, acumuladoracima, acumuladorabaixo))