num_a = int(input('Ingresar un numero: '))

factorial = 1
if num_a < 0:
    print("Para numeros negativos no existe factorial")
elif num_a == 0:
    print("El factoria de 0 es 1")
else:
    for i in range(1, num_a + 1):
        factorial *= i

print("El factorial de", num_a, "es", factorial)
    