alumnos, salvaron, aplazaron, entre_sesen_nov, mayor_nov = 0, 0, 0, 0, 0
while True:
    nota = int(input('Introducir la nota: '))

    if nota < 0:
        break

    alumnos += 1

    if 60 > item:
        aplazaron += 1
    elif 60 <= item <= 90:
        entre_sesen_nov += 1
        salvaron += 1
    elif 90 < item:
        mayor_nov += 1
        salvaron += 1

print(f"Alumnos que obtuvieron mas de 90 puntos: {mayor_nov}\n"
      f"Alumnos que obtuvieron entre 60 y 90: {entre_sesen_nov}\n"
      f"Alumnos que se aplazaron: {aplazaron}\n"
      f"Alumnos que salvaron: {salvaron}\n"
      f"Total de alumnos: {alumnos}")
