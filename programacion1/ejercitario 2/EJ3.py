cantidad_hom = 0
cantidad_muj = 0
while True:
    ingresar_alumn = input('Introducir datos de alumno(Si/No): ')

    if ingresar_alumn.upper() == 'SI':
        alumno = input('Ingresar sexo del alumno(0:hombre/1:mujer): ')
        if alumno == '0':
            cantidad_hom += 1
        elif alumno == '1':
            cantidad_muj += 1
        else:
            print('Ingresar 0 si es hombre o 1 si es mujer.')

    elif ingresar_alumn.upper() == 'NO':
        break

    else:
        print('Ingresar Si o No')

print(f"La contidad de hombres es: {cantidad_hom} y la cantidad de mujeres es: {cantidad_muj}")

