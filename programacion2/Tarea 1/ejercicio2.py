'''
ANALISIS DEL PROBLEMA:
    Tomar tres longitudes. Averiguar si es un triangulo rectangulo, y si lo es, averiguar el perimetro y el area.

BUSQUEDA DE RESULTADOS:
    -Hallar la longitud mas grande y poner como hipotenusa.
    -Ver si cumple el teorema de pitagoras h^2=c^2 + c^2
    -Si cumple el teorema hay que sumar los lados para hallar el perimetro
    -Porque no se sabe cual de las longitudes es la altura hay que usar la formula de Heron A = (S * (S - L1) * (S - L2) * (S - L3))^0.5
    -Hallar el semiperimetro S = P / 2
'''

# REDACCION DEL ALGORITMO:
longitudes = []

while len(longitudes) < 3:
    long = int(input('Ingresar los lados del triangulo: '))
    longitudes.append(long)

perimetro = sum(longitudes)
semiperi = perimetro / 2
area = (semiperi * (semiperi - longitudes[0]) * (semiperi - longitudes[1]) * (semiperi - longitudes[2])) ** 0.5

hipotenusa = max(longitudes)
longitudes.remove(hipotenusa)
catetos = longitudes

if hipotenusa ** 2 == (catetos[0] ** 2) + (catetos[1] ** 2):
            print('Es un triangulo rectangulo')
            print(f"PERIMETRO: {perimetro}\n"
                f"AREA: {area}")
else:
    print('No es un triangulo rectangulo')