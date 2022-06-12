num = int(input('Ingresar un numero: '))

acu = 0
suma_cumplen = 0
c = 0
for i in range(num):
    num_x = int(input('Ingresar un numero X: '))
    num_y = int(input('Ingresar un numero Y: '))
    num_z = int(input('Ingresar un numero Z: '))

    suma = num_x + num_y + num_z
    acu += suma
    if 220 < suma < 550:
       suma_cumplen += suma
       c += 1

if c > 0:
    prom = suma_cumplen/c
    print(f"El promedio de los que cumplieron la condicion es: {prom}")
else:
    prom_todos = acu/num * 3
    print(f"El promedio de los numeros leidos es: {prom_todos}")