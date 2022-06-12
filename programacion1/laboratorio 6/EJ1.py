num = int(input('Ingresar un numero: '))

suma, suma_cuadrado, suma_cubo = 0
for i in range(num):
    suma += i
    suma_cuadrado += i ** 2
    suma_cubo += i ** 3

print(f"La suma de todos los números enteros hasta N: {suma}\n"
      f"La suma de todos los números enteros hasta N elevados al cuadrado: {suma_cuadrado}\n"
      f"La suma de todos los números enteros hasta N elevados al cubo: {suma_cubo}\n"
      f"La suma de todos los números calculados en a, b, c: {suma + suma_cuadrado + suma_cubo}")
