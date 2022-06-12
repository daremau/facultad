nombre = input('Introduzca su nombre: ')
apellido = input('Introduzca su apellido: ')
edad = int(input('Introduzca su edad: '))
domicilio = input('Introduzca su domicilio: ')
num_cel = input('Introduzca su numero de celular: ')

nombre_compa = input('Introduzca el nombre de su compañero: ')
edad_compa = int(input('Introduzca la edad de su compañero: '))

suma_edades = edad + edad_compa

print(f'-----------------------------------------------------------------------')
print(f'\"Tu nombre es {nombre} tu APELLIDO es {apellido} y tienes {edad}\" \n'
      f'\"DOMICILIO: {domicilio} Numero de celular: {num_cel}\" \n'
      f'\"Tu compañero se llama {nombre_compa} y tiene {edad_compa} años\" \n'
      f'\"La SUMA de las dos edades es {suma_edades} años\"')
print(f'-----------------------------------------------------------------------')
