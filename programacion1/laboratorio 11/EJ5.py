n = int(input('Ingresar un numero: '))

vector_a = []
vector_b = []

for i in range(n):
    num_a = int(input('Ingresar otro numero para vector A: '))
    num_b = int(input('Ingresar otro numero para vector B: '))
    vector_a.append(num_a)
    vector_b.append(num_b)

vector_c = []
for i in range(n * 2):
    vector_c.append(1)

a = 0
b = 0
for i in range(len(vector_c)):
    if i % 2 == 0:
        vector_c[i] = vector_b[b] ** 0.5
        b += 1
    else:
        vector_c[i] = vector_a[a] ** 2
        a += 1
    

print(f"Vector C: {vector_c}")