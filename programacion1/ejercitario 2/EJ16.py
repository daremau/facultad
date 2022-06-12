suma_f = 0
for i in range(1000):
    x = int(input('Introducir un numero: '))
    
    if x > 0:
        f = x ** 0.5
        print(f'X: {x}. F: {f}')
    elif x == 0:
        f = 73
        print(f'X: {x}. F: {f}')
    elif x < 0:
        f = abs(x)
        print(f'X: {x}. F: {f}')
    
    suma_f += f

print(f"Suma de F: {suma_f}")
