n = int(input('Ingresar un numero: '))

vector_a = []
vector_b = []
suma_pares = 0
suma_impares = 0
p, im = 0, 0
mayor_a = None
mayor_b = None

for i in range(n):
    a = int(input('Ingresar otro numero para A: '))
    b = int(input('Ingresar otro numero para B: '))

    if mayor_a == None:
        mayor_a = a
    elif a > mayor_a:
        mayor_a = a
    
    if mayor_b == None:
        mayor_b = b
    elif b > mayor_b:
        mayor_b = b
    
    vector_a.append(a)
    vector_b.append(b)

    if vector_a[i] % 2 == 0:
        suma_pares += vector_a[i]
        p += 1
    
    if vector_b[i] % 2 != 0:
        suma_pares += vector_b[i]
        im += 1

if suma_pares != 0:
    print(f"El promedio de los numeros pares es: {suma_pares/p}, y la cantidad: {p}")
else:
    print('No se encontro el promedio del Vector A.')

if suma_impares != 0:
     print(f"El promedio de los numeros pares es: {suma_impares/im}, y la cantidad: {im}")
else:
    print('No se encontro el promedio del Vector B.')

contador_a = 0
contador_b = 0
for i in range(n):
    if vector_a[i] == mayor_a:
        contador_a += 1
    
    if vector_b[i] == mayor_b:
        contador_b += 1

print(f"El mayor numero en el Vector A es A({vector_a.index(mayor_a)})={mayor_a} y se repite {contador_a} veces.\n"
    f"El mayor numero en el Vector B es B({vector_b.index(mayor_b)})={mayor_b} y se repite {contador_b} veces.")