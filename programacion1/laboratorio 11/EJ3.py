n = int(input('Dimension del Vector: '))

vector_a = []
vector_b = []
posiciones = []
menor = None
for i in range(n):
    num = int(input('Ingresar un numero para el Vector A: '))
    vector_a.append(num)
    
    if menor is None:
        menor = num
    if num < menor:
        menor = num
    
    if num % 2 == 1:
        vector_b.append(num)

if vector_b:
    print(f"Primer componente del Vector A: {vector_a[0]}\n"
        f"Ultimo componente del vector A: {vector_a[-1]}")
else:
    for i in vector_a:
        if i == menor:
            posiciones.append(vector_a.index(i))
    print(f"El menor elemento de A es: {menor} y esta en las posiciones: {posiciones}")

