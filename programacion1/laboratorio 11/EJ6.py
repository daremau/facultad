n = int(input('Ingresar un numero: '))

vector_a = []
for i in range(n):
    num = int(input('Ingresar otro numero para vector A: '))
    vector_a.append(num)

vector_b = []

i = 0
while i < n:
    vector_b.append(vector_a[i])
    i += 1
i = 0
while i < n:
    vector_b.append(vector_a[i] ** 2)
    i += 1
i = 0
while i < n:
    vector_b.append(vector_a[i] ** 3)
    i += 1
i = 0
while i < n:
    vector_b.append(0)
    i += 1

print(f"Vector B: {vector_b}")