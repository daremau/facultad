arr = [1, 2, 3, 4, 5, 6]
def busqueda_binaria(objetivo, inicio, final):
    if inicio > final:
        return 'No hay'
    
    medio = round((inicio + final) / 2)

    if arr[medio] == objetivo:
        return f"Encontrado en indice {medio}"
    
    elif arr[medio] > objetivo:
       return busqueda_binaria(objetivo, inicio, medio - 1)

    elif arr[medio] < objetivo:
       return busqueda_binaria(objetivo, medio + 1, final)

print(busqueda_binaria(2, 1, 6))