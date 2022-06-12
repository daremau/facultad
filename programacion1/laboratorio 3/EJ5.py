num_x = int(input('Valor de X: '))
num_y = int(input('Valor de Y: '))

suma = num_x + num_y
mult = num_x * num_y
media = suma / 2

if mult > 0:
    num_r = ((num_x ** 2) + (num_y ** 2)) ** 0.5
    print(f'El producto es positivo y el numero R es {num_r}')

elif media > 15:
    num_r = abs(3 * (num_x ** 2) + 5 * (num_y ** 2))
    print(f'El promedio es mayor que 15 y el numero R es {num_r}')

else:
    print(f"El valor de X es {num_x} y el valor de Y es {num_y}\n"
          f"La suma de estos es {suma}, el producto es {mult} y el promedio es {media}")
