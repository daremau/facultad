n = int(input('Dimension del Vector: '))

vector_a = []
suma, c = 0, 0
for i in range(n):
    num = int(input('Ingresar un numero para el Vector A: '))
    vector_a.append(num)

suma_pares, p = 0, 0
componentes_cumplen = []
for i in vector_a:
    if i % 2 != 0 and i < 190:
        suma += i
        c += 1
        componentes_cumplen.append(i)
    
    if vector_a.index(i) % 2 == 0:
        suma_pares += i
        p += 1

if c == 0:
    print('No se pudo encontrar el promedio.\n'
        f"Promedio lugares pares: {suma_pares / p}")
else:
    print(f"El promedio es: {suma / c}\n"
        f"Componentes que cumplen la condicion: {componentes_cumplen}")
