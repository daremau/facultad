matriculas = [10, 20, 40]

P = int(input('Ingresar numero de alumnos que se inscribieron tarde: '))

for i in range(P):
    matriculas.append(int(input('Ingresar matricula: ')))

for i in range(len(matriculas)):
    indice_min = i
    for j in range(i + 1, len(matriculas)):
        if matriculas[indice_min] > matriculas[j]:
            indice_min = j
    matriculas[indice_min], matriculas[i] = matriculas[i], matriculas[indice_min]


print(matriculas)

