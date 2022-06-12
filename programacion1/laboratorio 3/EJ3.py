edad = int(input('Ingrese la edad: '))

if edad < 12:
    print(f'La edad de {edad} corresponde a un infante')

elif 12 < edad <= 16:
    print(f'La edad de {edad} corresponde a un pre-adolescente')

elif 16 < edad < 21:
    print(f'La edad de {edad} corresponde a un adolescente')

else:
    print(f'La edad de {edad} corresponde a un adulto')