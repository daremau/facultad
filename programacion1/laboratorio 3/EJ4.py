nombre = input('Ingresar un nombre: ')
zona = input('Ingresar zona de procedencia (1:Urbana, 2:Periferica o 3:Rural): ')

if zona == '1':
    print(f'{nombre} corresponde a la zona urbana')

elif zona == '2':
    print(f'{nombre} corresponde a la zona periferica')

elif zona == '3':
    print(f'{nombre} corresponde a la zona rural')

else:
    print('Ingresar un numero del 1 al 3')
