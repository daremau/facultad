num_a = int(input('Valor de A: '))

if num_a % 2 == 0 and num_a % 3 == 0:
    print(f'{num_a} es multiplo de 2 y 3')

elif num_a % 2 == 0:
    print(f'{num_a} es multiplo de 2 solamente')

elif num_a % 3 == 0:
    print(f'{num_a} es multiplo de 3 solamente')

else:
    print(f'{num_a} no es multiplo de 2 ni de 3')