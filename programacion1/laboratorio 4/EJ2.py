num = int(input("Ingresar un numero: "))
sum_d_sum = 0

for i in range(num):
    num_x = int(input('Ingresar numero X: '))

    doble = num_x * 2
    cuadrado = num_x ** 2
    cubo = num_x ** 3
    sqr = num_x ** 0.5
    suma = doble + cuadrado + cubo + sqr
    
    print(f"El numero X es: {num_x} y su doble: {doble}, cuadrado: {cuadrado}, cubo: {cubo}, raiz:{sqr:.2f}\n"
          f"Suma de operaciones: {suma}")

    sum_d_sum += suma

print(f"La suma de la sumas es: {sum_d_sum}")