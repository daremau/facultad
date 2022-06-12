num_ci = int(input('Numero de CI: '))
nombre = input('Ingrese su nombre: ')
apellido = input('Ingrese su apellido: ')
edad = int(input('Ingrese su edad: '))

if edad >= 18:
    print(f'{nombre} {apellido} ya eres mayor de edad')
else:
    print(f'{nombre} {apellido} todavia te faltan {18 - edad} para ser mayor de edad')