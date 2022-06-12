n = int(input('Dimension del Vector: '))

vector = []
vector_rotado = []
for i in range(n):
    num = int(input('Ingresar un numero: '))
    vector.append(num)

print(f"Vector antes: {vector}")

#vector = [vector[-1]] + vector[:-1]
for i in range(n - 1):
    vector_rotado.append(vector[i])

print(f"Vector despues: {vector_rotado}")
