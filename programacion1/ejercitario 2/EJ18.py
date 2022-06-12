alumnos = int(input('Ingresar cantidad de alumnos: '))

mayor, menor = None, None
mayor_nom, mayor_sexo, menor_nom, menor_sexo = 0, 0, 0, 0
for i in range(alumnos):
    id = input('Ingresar id: ')
    nombre = input('Ingresar nombre: ')
    sexo = input('Ingresar sexo: ')
    prom = int(input('Ingresar promedio: '))

    if mayor is None:
        mayor = sueldo
        mayor_nom = nombre
        mayor_sexo = sexo

        menor = sueldo
        menor_nom = nombre
        menor_sexo = sexo
    elif sueldo > mayor:
        mayor = sueldo
        mayor_nom = nombre
        mayor_sexo = sexo

    if menor < sueldo:
        menor = sueldo
        menor_nom = nombre
        menor_sexo = sexo
