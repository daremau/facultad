arr = [2, 6, 3, 1, 4, 5]

# 1(a)
def ordenamiento_max(arr):
    for i in range(len(arr) - 1, -1, -1):
        indice_max = i
        for j in range(len(arr) - 1, i - 1, -1):
            if arr[i] > arr[j]:
                indice_max = j
        
        arr[i], arr[indice_max] = arr[indice_max], arr[i]
    
    return arr

# print(ordenamiento_max(arr))

# 1(b)
def ordenamiento_minmax(arr):
    indice_min = 0
    indice_max = len(arr) - 1

    while indice_max > indice_min:
        for i in range(indice_min, indice_max):
            if arr[i] < arr[indice_min]:
                arr[i], arr[indice_min] = arr[indice_min], arr[i]
            
            if arr[i] > arr[indice_max]:
                arr[i], arr[indice_max] = arr[indice_max], arr[i]
        
        indice_min += 1
        indice_max -= 1
    
    return arr

# print(ordenamiento_minmax(arr))

# 1(c)
def ord_burbuja_final(arr):
    ordenado = False
    while not ordenado:
        ordenado = True
        for i in range(len(arr) - 1, 0, -1):
            if arr[i] < arr[i - 1]:
                ordenado = False
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
    
    return arr

# print(ord_burbuja_final(arr))

# 1(d)
def ord_burbuja_intercalado(arr):
    ordenado = False
    cambio = 0
    while not ordenado:
        ordenado = True
        if cambio % 2 == 0:
            inicio = 0
            final = len(arr) - 1
            step = 1

            for i in range(inicio, final, step):
                if arr[i] > arr[i + 1]:
                    ordenado = False
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
        else:
            inicio = len(arr) - 1
            final = 0
            step = -1
            for i in range(inicio, final, step):
                if arr[i] < arr[i - 1]:
                    ordenado = False
                    arr[i], arr[i - 1] = arr[i - 1], arr[i]
        
        cambio += 1
    
    return arr

print(ord_burbuja_intercalado(arr))