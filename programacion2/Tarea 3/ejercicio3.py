arr1 = [1, 5, 9, 30]
arr2 = [3, 4, 8, 50]

arr3 = arr1 + arr2


for i in range(len(arr3)):
    indice_min = i
    for j in range(i + 1, len(arr3)):
        if arr3[indice_min] > arr3[j]:
            indice_min = j
    arr3[indice_min], arr3[i] = arr3[i], arr3[indice_min]

print(arr3)