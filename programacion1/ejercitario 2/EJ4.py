for i in range(1000):
    num_x = int(input('Ingresar numero X: '))

    if num_x >= 5:
        num_f = num_x**2 - num_x

    elif -2 <= num_x <= 5:
        num_f = 71

    elif num_x <= -2:
        num_f = num_x + 10

    print(f"El nUmero X es: {num_x} y el numero F es: {num_f}")

