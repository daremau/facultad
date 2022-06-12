num_m = int(input('Ingresar numero M: '))
num_n = int(input('Ingresar numero N: '))

n, suma = 0, 0
producto = 1
if num_m >= num_n:
    print('M debe ser menor que N')
else:
    for i in range(num_m + 1, num_n):
        n += 1
        suma += i
        producto *= i

if n == 0:
    n = 1
print(f"La suma de los numeros entre M y N es: {suma}\n"
      f"El producto de los numeros entre M y N es:{producto}\n"
      f"El promedio de los numeros entre M y N es: {suma/n}")
