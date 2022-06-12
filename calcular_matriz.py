import numpy as np

matriz_enero = np.matrix('9 5 2 ; 3 8 0 ; 0 0 0 ; 6 7 -1')
matriz_febrero = np.matrix('5 2 3 ; 6 6 6 ; 4 0 0 ; 0 0 0')
print('Matriz enero:')
print(matriz_enero)
print('Matriz febrero:')
print(matriz_febrero)

matriz_ventas_conjuntas = matriz_enero + matriz_febrero
print('Matriz de ventas conjuntas:')
print(matriz_ventas_conjuntas)

matriz_variacion = matriz_febrero - matriz_enero
print('Matriz de variacion:')
print(matriz_variacion)

matriz_marzo = 2 * matriz_enero
print('Matriz de marzo:')
print(matriz_marzo)
matriz_abril = 4 * matriz_marzo
print('Matriz de abril:')
print(matriz_abril)

matriz_cuatrimestre = matriz_ventas_conjuntas + matriz_marzo + matriz_abril
print('Matriz de cuatrimestre:')
print(matriz_cuatrimestre)