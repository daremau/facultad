from statistics import mean

n = int(input('Ingresar un numero: '))

vector_a = []
vector_b = []
vector_d = []
vector_c = []
vector_e = []

for i in range(n):
    num_a = int(input('Ingresar otro numero para vector A: '))
    num_b = int(input('Ingresar otro numero para vector B: '))
    vector_a.append(num_a)
    vector_b.append(num_b)

for i in range(n):
    vector_c.append(vector_a[i] - vector_b[i])

    vector_d.append(vector_a[i] - min(vector_b))

    vector_e.append(vector_b[i] - mean(vector_b))

print(f"Vector C: {vector_c}\n"
    f"Vector D: {vector_d}\n"
    f"Vector E: {vector_e}")