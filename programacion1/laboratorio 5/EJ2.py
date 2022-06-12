num = int(input('Ingresar un numero N: '))

cuenta = []
no_cuenta = []
promedio = 0
for i in range(num):
    num_x = int(input('Ingresar un numero X: '))
    if num_x % 3 == 0 and 100 < num_x < 300:
        cuenta.append(num_x)

    else:
        no_cuenta.append(num_x)
try:
    promedio = sum(cuenta)/len(cuenta)
    print(f'El promedio de los numero es: {promedio} con {len(cuenta)} que cumplieron la condicion')
except ZeroDivisionError:
    print('No se pudo crear el promedio deseado\n'
          f'El promedio de los numero leidos es: {sum(no_cuenta)/len(no_cuenta)}')
