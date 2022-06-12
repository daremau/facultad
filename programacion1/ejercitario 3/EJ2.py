n = int(input('Ingresar dimesion de los vectores: '))

vector_a = []
vector_b = []
vector_c = []

for i in range(n):
    num_a = int(input('Ingresar un numero para Vector A: '))
    num_b = int(input('Ingresar un numero para Vector B: '))

    vector_a.append(num_a)
    vector_b.append(num_b)
    vector_c.append(num_a + num_b)

print(f"Vector A: {vector_a}\n"
      f"Vector B: {vector_b}\n"
      f"Vector C: {vector_c}")

