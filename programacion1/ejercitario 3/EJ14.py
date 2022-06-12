n = int(input('Dimension del vector: '))

vector = []
vector_comprimido =[]
for i in range(n):
    num = int(input('Ingresar un numero: '))
    vector.append(num)

    if num != 0:
        vector_comprimido.append(num)

c = 0
for i in vector_comprimido:
    c += 1

if not vector_comprimido:
    print('Todas las compentes del vector son cero.')
else:
    print(f"Vector normal: {vector}, con dimension: {n}\n"
          f"Vector comprimido: {vector_comprimido}, con dimension: {c}")
