num_mes = int(input('Numero del mes: '))

if num_mes < 13:
    if num_mes in [1, 3, 5, 7, 8, 10, 12]:
        print('El mes tiene 31 dias')
    elif num_mes in [4, 6, 9, 11]:
        print('El mes tiene 30 dias')
    else:
        print('El mes tiene 28 o 29 dias')
else:
    print('No hay mas de doce meses')