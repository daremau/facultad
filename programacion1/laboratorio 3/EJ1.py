num_a = int(input('Valor de numero A: '))

if num_a % 2 == 0 and num_a % 3 == 0:
    print(f'{num_a} Es múltiplo de 2 y de 3') 

elif num_a % 2 == 0:
    print(f'{num_a} es múltiplo de 2 solamente')

elif num_a % 3 == 0:
    print(f'{num_a} Es múltiplo de 3 solamente')

else:
    print(f'{num_a} No es múltiplo de 2 ni de 3')

