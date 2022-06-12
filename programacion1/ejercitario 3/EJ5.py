n = int(input('Ingresar dimension del vector: '))

vector_a = []
vector_b = []
vector_c = []
for i in range(n):
    vector_a.append(i)
    vector_b.append(i * 2)
    vector_c.append(0)

print(f"Primero: {vector_a}\n"
      f"Segundo: {vector_b}\n"
      f"Tercero: {vector_c}")
