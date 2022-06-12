num_a = int(input('Valor de numero A: '))
num_b = int(input('Valor de numero B: '))

if num_a % 2 == 0 and num_b % 3 == 0:
    print(f'{num_a} es multiplo de 2 y {num_b} es multiplo de 3')

elif num_a % 2 == 0:
    print(f'{num_a} es multiplo de 2 pero {num_b} no es multiplo de 3')

elif num_b % 3 == 0:
    print(f'{num_a} no es multiplo de 2 y {num_b} es multiplo de 3')

else:
    print(f'{num_a} no es multiplo de 2 y {num_b} no es multiplo de 3')