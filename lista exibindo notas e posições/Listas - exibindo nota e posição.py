numerosDeNotas = int(input())
listaVazia = []
somatorio = 0
if 0 < numerosDeNotas <=5:
    for i in range(numerosDeNotas):
        nota = float(input())
        listaVazia.append(nota)
        somatorio += nota
        
    media = somatorio/numerosDeNotas

    for i in range(numerosDeNotas):
        print('Nota ' + str(i+1) + ': ' + str(listaVazia[i]))
    
    print('{:.2f}'.format(media))

else:
    print('Numero de notas invalido.')