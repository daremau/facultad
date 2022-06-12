n = int(input('Ingresar un numero: '))

vector_a = []
c = 0
suma = 0
menor = None
for i in range(n):
    a = int(input('Ingresar otro numero: '))
    if a <= 20:
        suma += a
        c += 1

    vector_a.append(a)

    if menor == None:
        menor = a
    elif a < menor:
        menor = a

if c == 0:
    print('No se pudo encontrar el promedio.')
else:
    print(f"El promedio es {suma/c} y la cantidad de elementos que cumplieron la condicion es: {c}")

print(f'EL menor de los elemntos es A({vector_a.index(menor)})={menor}')
