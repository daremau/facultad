m = int(input('Ingresar un numero: '))

vector_a = []
vector_b = []
vector_c = []
sum_no_cero, sum_impares, c, im = 0, 0, 0, 0
mayor_a = None
mayor_b = None
for i in range(m):
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

    if a != 0:
        sum_no_cero += a
        c += 1
    
    if b % 2 != 0:
        sum_impares += b
        im += 1

    vector_a.append(a)
    vector_b.append(b)

if mayor_a > mayor_b:
    vector_c.append(mayor_a)
else:
    vector_c.append(mayor_b)

if c != 0:
    print(f"El promedio de A es: {sum_no_cero / c}")
else:
    print('No se pudo calcular el promedio.')

if im != 0:
    print(f"El promedio de B es: {sum_impares / im}")
else:
    print('No se pudo calcular el promedio')

print(vector_c)
print(f"El menor elemento del Vector C es: {vector_c[0]}")