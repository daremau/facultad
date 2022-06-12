num = int(input('Ingresar un numero: '))

sum_cuadra = 0
for i in range(num):
    doble = i*2
    cuadra = i**2
    sum_cuadra += cuadra
    print(f'El numero es : {i} y su doble: {doble}, cuadrado: {cuadra}')

print(f"La suma de los cuadrados es: {sum_cuadra}")