while True:
    lista1 = []
    lista2 = []
    lista_str = input().split()
    lista_int = []
    nome1=[]
    nome2=[]
    if lista_str[-1] == 'sair':
        print('fim')
        break
    else:
        nome1.append(lista_str[0])
        lista_str.pop(0)
        nome2.append(lista_str[0])
        lista_str.pop(0)
        for c in range(len(lista_str)):
            lista_int.append(int(lista_str[c]))
        x = len(lista_int)
        if len(lista_str) % 2 == 1:
            print('erro')
            break
        
        else:
            somatorio1 = 0
            somatorio2 = 0
            for i in range(x//4):
                for c in range(2):
                    lista1.append(lista_int[0])
                    lista_int.pop(0)
                for x in range(2):
                    lista2.append(lista_int[0])
                    lista_int.pop(0)
            for z in range(len(lista1)//2):
                if lista1[0] == lista1[1]:
                    somatorio1 += (lista1[0] + lista1[1]) * 2
                elif lista1[1] - 1 == lista1[0] or lista1[0] - 1 == lista1[1] or lista1[1] + 1 == lista1[0] or lista1[0] + 1 == lista1[1]:
                    somatorio1 += (lista1[0] + lista1[1]) * 3
                else:
                    somatorio1+=lista1[0]+lista1[1]
                lista1.pop(0)
                lista1.pop(0)
            for t in range(len(lista2)//2):
                if lista2[0] == lista2[1]:
                    somatorio2 += (lista2[0] + lista2[1]) * 2
                elif lista2[1] - 1 == lista2[0] or lista2[0] - 1 == lista2[1] or lista2[1] + 1 == lista2[0] or lista2[0] + 1 == lista2[1]:
                    somatorio2 += (lista2[0] + lista2[1]) * 3
                else:
                    somatorio2+=lista2[0]+lista2[1]
                lista2.pop(0)
                lista2.pop(0)
            if somatorio1 > somatorio2:
                print(nome1[0])
            elif somatorio1 == somatorio2:
                print('empate')
            else:
                print(nome2[0])
                