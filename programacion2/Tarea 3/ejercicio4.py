alumnos = []

N = int(input('Ingresar numero de alumnos: '))

for i in range(N):
    alumnos.append(int(input('Ingresar matricula: ')))

alumnos1 = alumnos[:round(N/2)]
alumnos2 = alumnos[round(N/2):]

def ordenar_lista(arr):
    for i in range(len(arr)):
        indice_min = i
        for j in range(i + 1, len(arr)):
            if arr[indice_min] > arr[j]:
                indice_min = j
        
        arr[indice_min], arr[i] = arr[i], arr[indice_min]
    
    return arr

alumnos1 = ordenar_lista(alumnos1)
alumnos2 = ordenar_lista(alumnos2)

alumnos = alumnos1 + alumnos2

print(ordenar_lista(alumnos))