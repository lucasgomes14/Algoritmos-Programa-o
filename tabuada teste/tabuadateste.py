num1 = int(input('22'))
num2 = int(input('11'))
if num1 < 1:
    print('Insira um número inicial entre 1 e 9')
    for num1 in range(1):
    
elif num2 > 9:
    print('Insira um número final entre 1 e 9')
    for num2 in range(1):
    
elif 0 < num1 < 10 and 0 < num2 < 10 and num1 < num2:
    for x in range(num1,num2 + 1):
        um = x * 1
        dois = x * 2
        tres = x * 3
        quatro = x * 4
        cinco = x * 5
        seis = x * 6
        sete = x * 7
        oito = x * 8
        nove = x * 9
        print('{} x 1 = {}\n{} x 2 = {}\n{} x 3 = {}\n{} x 4 = {}\n{} x 5 = {}\n{} x 6 = {}\n{} x 7 = {}\n{} x 8 = {}\n{} x 9 = {}\n'.format(x,um,x,dois,x,tres,x,quatro,x,cinco,x,seis,x,sete,x,oito,x,nove))
elif num1 > 0 and num2 < 10 and num1 == num2:
    for x in range(num1,num2 + 1):
        um = x * 1
        dois = x * 2
        tres = x * 3
        quatro = x * 4
        cinco = x * 5
        seis = x * 6
        sete = x * 7
        oito = x * 8
        nove = x * 9
        print('{} x 1 = {}\n{} x 2 = {}\n{} x 3 = {}\n{} x 4 = {}\n{} x 5 = {}\n{} x 6 = {}\n{} x 7 = {}\n{} x 8 = {}\n{} x 9 = {}\n'.format(x, um, x, dois, x, tres, x, quatro, x, cinco, x, seis, x, sete, x, oito, x, nove))
elif num1 > 0 and num2 < 10 and num2 > num1:
    print('Nenhuma tabuada nesse intervalo')