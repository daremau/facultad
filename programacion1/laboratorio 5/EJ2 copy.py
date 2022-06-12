num = int(input('Ingresar un numero N: '))

cuenta = 0
promedio = 0
falso_promedio = 0
for i in range(num):
    num_x = int(input('Ingresar un numero X: '))
    if num_x % 2 != 0 and 100 < num_x < 300:
        cuenta += 1
        promedio += num_x
        
    else:
        falso_promedio += num_x
        print(f"El numero {num_x} no puede ser agregado agregado al promedio\n"
              f"El promedio actual de los numero leidos es: {falso_promedio}")

print(f"El promedio es: {promedio}\n"
      f"La cantidad de elementos que cumplieron la condicion es: {cuenta}")