comida=input().upper()
bebida=input().upper()
contador=0
if comida == 'LASANHA':
    contador+=8.00
else:
    contador+=11.00
if bebida == 'REFRIGERANTE':
    contador+=3.00
else:
    contador+=2.50
print('{:.2f}'.format(contador))
