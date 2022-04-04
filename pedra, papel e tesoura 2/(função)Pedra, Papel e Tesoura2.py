#funções
def ler_jogada():
    maria = input().lower()
    miguel = input().lower()
    return maria,miguel

def partida(jog_maria,jog_miguel):
    if (jog_maria == 'pedra' and jog_miguel == 'tesoura') or \
       (jog_maria == 'papel' and jog_miguel == 'pedra') or \
       (jog_maria == 'tesoura' and jog_miguel == 'papel'):
        return 'vitoria_maria'
    elif jog_miguel == jog_maria:
        return 'empate'
    else:
        return 'vitoria_miguel'

#programa principal

cont = 1
vitoria_miguel = vitoria_maria = 0

while cont < 6:
    
    jogada_maria,jogada_miguel = ler_jogada()
    
    if partida(jogada_maria,jogada_miguel) == 'vitoria_miguel':
        vitoria_miguel += 1
    elif partida(jogada_miguel,jogada_maria) == 'empate':
        continue
    else:
        vitoria_maria += 1
        
    cont += 1
if vitoria_miguel > vitoria_maria:
    print('MIGUEL')
else:
    print('MARIA')