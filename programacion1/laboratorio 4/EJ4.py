num = int(input('Ingresar un numero: '))

sum_raiz = 0
sum_numx = 0
for i in range(num):
    num_x = int(input('Ingresar otro numero: '))
    num_x += 1
    
    if num_x % 2 == 0:
        raiz = i ** 0.5
        sum_raiz += raiz
        sum_numx += num_x
    
    else:
        raiz = abs(i ** (1 / 3)) 
        sum_raiz += raiz
        sum_numx += num_x
    
    print(f"El numero es: {num_x} y su raiz: {raiz}")

suma = sum_numx + sum_raiz

print(f"La suma de todos los numero es: {sum_numx} y la suma de todos los valores calculados: {suma}")