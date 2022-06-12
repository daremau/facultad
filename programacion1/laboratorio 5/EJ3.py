varones = 0
nota_varon = 0
mujeres = 0
nota_mujer = 0
total = 0
nota_total = 0
dic = {}
while True:
    id = int(input('Ingresar ID de alumno: '))
    if id < 0:
        print('El ID debe ser positivo.')
        break
    
    nombre = input('Ingresar nombre del alumno: ')
    calific = int(input('Ingresar calificacion del alumno: '))
    
    sexo = int(input('Ingresar sexo del alumno(0-masculino, 1-femenino): '))
    if sexo == 0:
        varones += 1
        nota_varon += calific
        dic[nombre] = calific
    elif sexo == 1:
        mujeres += 1
        nota_mujer += calific
    
    total += 1
    nota_total += calific

try:
    print(f"PROMEDIO DE VARONES: {nota_varon/varones}\n"
        f"CANTIDAD DE VARONES: {varones}\n"
        f"PROMEDIO MUJERES: {nota_mujer/mujeres}\n"
        f"CANTIDAD DE MUJERES: {mujeres}\n"
        f"PROMEDIO TOTAL: {nota_total/total}\n"
        f"CANTIDAD TOTAL DE ALUMNOS: {total}\n"
        f"La menor calificacion de los varones corresponde a: {min(dic, key=dic.get)}")
except ZeroDivisionError:
    pass
