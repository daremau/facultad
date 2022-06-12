n = int(input('Dimension Vector A: '))
m = int(input('Dimension Vector B: '))
vector_a = []
vector_b = []

suma_a, a, suma_b, b = 0, 0, 0, 0
componentes_cumplen_a = []
componentes_cumplen_b = []
for i in range(n):
    num_a = int(input('Ingresar otro numero para vector A: '))
    vector_a.append(num_a)

for i in range(m):
    num_b = int(input('Ingresar otro numero para vector B: '))
    vector_b.append(num_b)

for i in vector_a:
    if i % 2 != 0 and i > 40:
        suma_a += i
        a += 1
        componentes_cumplen_a.append(i)

for i in vector_b:
    if i % 2 == 0:
        suma_b += i
        b += 1
        componentes_cumplen_b.append(i)

if a == 0 or b == 0:
    print('No se pudo encontrar uno de los promedios')
else:
    print(f"Promedio de Vector A: {suma_a / a}\n"
        f"Promedio de Vector B: {suma_b / b}")
