n = int(input('Ingresar un numero: '))

vector_a = []
vector_c = []
vector_d = []
for i in range(n):
    num = int(input('Ingresar otro numero para vector A: '))
    vector_a.append(num)

    if num % 2 == 0:
        vector_c.append(num)
    
    if num != 0:
        vector_d.append(num)

print(f"Vector C: {vector_c}\n"
    f"Vector D: {vector_d}")

