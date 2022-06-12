notas = []
alumnos = int(input("¿Cuántos alumnos hay?: "))
debajo_media = 0
cat_1 = 0
cat_2 = 0
cat_3 = 0
cat_4 = 0
cat_5 = 0

i = 0
while i < alumnos:
    notas.append(int(input("Introduce la nota del alumno: ")))
    i += 1

mayor_nota = max(notas)
menor_nota = min(notas)
media = sum(notas) / alumnos

for nota in notas:
    if nota < media:
        debajo_media += 1

    if 1 < nota < 20:
        cat_1 += 1
    elif 20 < nota <= 40:
        cat_2 += 1
    elif 40 < nota <= 60:
        cat_3 += 1
    elif 60 < nota <= 80:
        cat_4 += 1
    elif 80 < nota <= 100:
        cat_5 += 1 

print("Nota         Cantidad\n"
        f"1-20            {cat_1}\n"
        f"21-40           {cat_2}\n"
        f"41-60           {cat_3}\n"
        f"61-80           {cat_4}\n"
        f"81-100          {cat_5}\n")

print(f"La nota más alta es {mayor_nota}\n"
      f"La nota más baja es {menor_nota}\n"
      f"La media de las notas es {media}\n"
      f"Hay {debajo_media} alumnos que se encuentran por debajo del promedio")