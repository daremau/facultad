num_a = int(input('El valor de A es: '))
num_b = int(input('El valor de C es: '))
num_c = int(input('El valor de B es: '))

menor = 0
if num_a < num_b and num_a < num_c:
    menor = num_a
elif num_b < num_a and num_b < num_c:
    menor = num_b
elif num_c < num_a and num_c < num_b:
    menor = num_c

print(f'El numero menor es {menor}')