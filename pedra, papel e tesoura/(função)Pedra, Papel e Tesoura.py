def pedra(outro):                          #caso o usuário escolha pedra
    if outro == 'tesoura':
        return('ganhou')
    elif outro == 'papel':
        return('perdeu')
    else:
        return('empate')
        
def papel(outro):                         #caso o usuário escolha papel
    if outro == 'pedra':
        return('ganhou')
    elif outro == 'tesoura':
        return('perdeu')
    else:
        return('empate')
    
def tesoura(outro):                     #caso o usuário escolha tesoura
    if outro == 'papel':
        return('ganhou')
    elif outro == 'pedra':
        return('perdeu')
    else:
        return('empate')
    
mariaresultado = miguelresultado = 0
cont = 1

while cont < 6:
    
    maria = input().lower()
    miguel = input().lower()
    
    if maria == 'pedra':
        disputa = pedra(miguel)
        if disputa == 'ganhou':
            mariaresultado += 1
        elif disputa == 'perdeu':
            miguelresultado += 1
        else:
            continue
    elif maria == 'papel':
        disputa == papel(miguel)
        if disputa == 'ganhou':
            mariaresultado += 1
        elif disputa == 'perdeu':
            miguelresultado += 1
        else:
            continue
    else:
        if disputa == 'ganhou':
            mariaresultado += 1
        elif disputa == 'perdeu':
            miguelresultado += 1
        else:
            continue
    cont += 1
    
if mariaresultado > miguelresultado:
    print('MARIA')
else:
    print('MIGUEL')