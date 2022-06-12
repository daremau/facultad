num = int(input("Ingresar un numero: "))
sum_d_sum = 0

for i in range(num + 1):
    doble = i * 2
    cuadrado = i ** 2
    cubo = i ** 3
    sqr = i ** 0.5
    suma = doble + cuadrado + cubo + sqr
    
    print(f"El numero n es: {i}y su doble: {doble}, cuadrado: {cuadrado}, cubo: {cubo}, raiz:{sqr:.2f}\n"
          f"Suma de operaciones: {suma}")

    sum_d_sum += suma

print(f"la sumas de la sumas es: {sum_d_sum}")