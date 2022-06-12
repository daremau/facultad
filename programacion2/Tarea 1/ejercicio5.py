'''
ANALISIS DEL PROBLEMA:
    -Ir eliminando elementos de la lista con el conteo de un numero N mayor a 3 y menor que 11
    empezando desde una posicion aleatoria hasta que quede solo un elemento

BUSQUEDA DE RESULTADOS:
    -Utilizar el modulo random para generar una posicion inicial aleatoria y N aleatorios
    -Utilizar un ncontador para iterar las posiciones.
    -Si el contador es mayor que la longitud de la lista, asignarlo a 0
    -Seguir sumando hasta iterar N veces las posiciones y eliminar el elemento que esta en la posicion donde paro el contador
    -Repetir hasta que en la lista solo que de un elemento
'''

# REDACCION DEL ALGORITMO:
import random

ronda = [[1, 2, 3, 4, 5, 6]]
numeros = []
for i in range(6):
    numeros.append(random.randrange(3, 11))
ronda.append(numeros)

print(ronda)

random_index = random.randrange(0, len(ronda[0]))
N = ronda[1][random_index]
print('elemento: ', ronda[0][random_index])
print('N: ', N)

while len(ronda[0]) > 1:
    for i in range(N - 1):
        random_index += 1
        if random_index >= len(ronda[0]):
            random_index = 0
        print(ronda[0][random_index])
    print(f"Se elimina el {ronda[0][random_index]}")
    ronda[0].pop(random_index)
    ronda[1].pop(random_index)

print(f"El ultimo elemento es: {ronda[0][0]}")
