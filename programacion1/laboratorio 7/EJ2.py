sum_edad, alum_sexto  = 0, 0
mayor = None
while True:
    id = int(input('Ingresar el ID: '))
    if id == -999:
        break
    nombre = input('Ingresar nombre: ')
    curso = int(input('Ingresar curso: '))
    sexo = int(input('Ingresar sexo(1:masculino, 2:femenino): '))
    edad = int(input('Ingresar edad: '))

    if curso == 6:
        sum_edad += edad
        alum_sexto += 1
        if sexo == 1:
            if mayor is None:
                mayor = edad
                nom_mayor = nombre
            elif edad > mayor:
                mayor = edad
                nom_mayor = nombre

if alum_sexto == 0:
    alum_sexto = 1
print(f"PROMEDIO DE LAS EDADES DEL SEXTO CURSO: {sum_edad / alum_sexto}\n"
      f"ALUMNO VARON CON MAYOR EDAD: {nom_mayor}, EDAD: {mayor}")
