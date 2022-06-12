'''
ANALISIS DEL PROBLEMA:
    -Sumar dos fracciones e imprimir el resultado en forma de fraccion.

BUSQUEDA DE RESULTADOS:
    -Si los denominadores son iguales, sumar solo los numeradores
    -Si son diferentes, multiplicar numerador 1 por denominador 2 y denominador 1 por numerador 2, 
        sumar las dos multiplicaciones y dividir por la multiplicacion de los denominadores
'''

# REDACCION DEL ALGORITMO:
numerador1 = int(input('Ingresar primer numerador: '))
denominador1 = int(input('Ingresar primer denominador: '))

numerador2 = int(input('Ingresar segundo numerador: '))
denominador2 = int(input('Ingresar segundo denominador: '))

if denominador1 == denominador2:
    numerador = numerador1 + numerador2
    print(f"La fraccion resultante es: {numerador} / {denominador1}")

elif denominador1 == 0 or denominador2 == 0:
    print('No tiene solucion')

else:
    numerador = (numerador1 * denominador2) + (denominador1 * numerador2)
    denominador = denominador1 * denominador2
    print(f"La fraccion resultante es: {numerador} / {denominador}")