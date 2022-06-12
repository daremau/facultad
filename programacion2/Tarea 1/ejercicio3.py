'''
ANALISIS DEL PROBLEMA:
    -Encontrar los valores de x e y que satisface a el sistema de ecuaciones.
    -Si el sistema no tiene solucion imprimir un mensaje.

BUSQUEDA DE RESULTADOS:
    -Resolver el sistema usando matrices
    -Ax + By = C
     Dx + Ey = F
     
    [[A, B], [D, E]] * [x, y] = [C, F]
       
       A  *  x  =  B
    
    x = A(inversa) * B  

    A(inversa) = 1/determinanteA * [[F, -B], [-D, A]]

    determinante = (A * E) - (D * B)
    
    -Si la determinante da cero siginifica que la matriz no se puede invertir, osea el sistema no tiene soluciones.
'''

# REDACCION DEL ALGORITMO:
A = float(input('Ingresar A: '))
B = float(input('Ingresar B: '))
C = float(input('Ingresar C: '))
D = float(input('Ingresar D: '))
E = float(input('Ingresar E: '))
F = float(input('Ingresar F: '))

determinante = (A * E) - (D * B)
if determinante == 0:
    print('El sistema de ecuaciones no tiene solucion')
else:
    solucion = []

    matriz_A = [
        [F, -B],
        [-D, A]
    ]

    matriz_B = [C, F]

    for i in range(len(matriz_A)):
        for j in range(len(matriz_A[i])):
            matriz_A[i][j] *= (1/determinante)

    for i in range(len(matriz_A)):
        for j in range(len(matriz_A[i])):
            incognita = matriz_A[i][j] * matriz_B[i]
            solucion.append(incognita)

    print(f"X = {solucion[0]}, Y = {solucion[1]}")