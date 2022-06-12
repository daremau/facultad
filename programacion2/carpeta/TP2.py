from numpy        import matrix as matriz; 
from numpy.linalg import inv as inversa;
from numpy        import set_printoptions
from numpy        import asarray
set_printoptions(formatter={'float': '{: 0.3f}'.format})
def Imprimir(Residencia, Matriz_A, Matriz_B, Inversa_A, X):
    # Formatear
    def    Cyan(Texto: str) -> str: return F"\x1b[36m{      Texto}\x1b[0m"
    def   Green(Texto: str) -> str: return F"\x1b[32m{      Texto}\x1b[0m"
    def  Orange(Texto: str) -> str: return F"\x1b[38;5;208m{Texto}\x1b[0m"
    def Limpiar_terminal(): print("\x1bc")
    
    # Convertir a array
    Matriz_A  = asarray( Matriz_A)
    Matriz_B  = asarray( Matriz_B)
    Inversa_A = asarray(Inversa_A)
    X         = asarray(        X)
    
    # Limpiar ANTERIOR
    Limpiar_terminal()

    # Simular SOLUCION
    print(F"""{Orange(Residencia)}

    {Cyan("DATOS")}
    Matriz_A: {Green("[")}
        {Green(Matriz_A[0])},
        {Green(Matriz_A[1])},
        {Green(Matriz_A[2])}
    {Green("]")}
    Matriz_B: {Green("[")}
        {Green(Matriz_B[0])},
        {Green(Matriz_B[1])},
        {Green(Matriz_B[2])}
    {Green("]")}

    {Cyan("SOLUCION")}
    {Cyan("1.")} Resolver {Cyan("Inversa_A")}: {Green("[")}
        {Green(Inversa_A[0])},
        {Green(Inversa_A[1])},
        {Green(Inversa_A[2])}
    {Green("]")}

    {Cyan("2.")} Resolver {Cyan("Inversa_A")} * {Cyan("Matriz_B")}: {Green("[")}
        {Green(X[0])},
        {Green(X[1])},
        {Green(X[2])}
    {Green("]")}
    """)

def Resolver(Residencia: str, Habitaciones: int, Plazas: int, Empleados: int):
    # Matriz_A:[
    #    [  X,   Y,   Z]      [  1,   1,   1] # Habitaciones 
    #    [  X,  2Y,  4Z]  >>  [1•1, 1•2, 1•4] # Plazas
    #    [X/9, Y/6, Z/4]      [1/9, 1/6, 1/3] # Empleados
    # ]
    
    Matriz_A  = matriz([
        [  1,   1,   1],
        [  1,   2,   4],
        [1/9, 1/6, 1/3]
    ])
    Matriz_B  = matriz([
        [Habitaciones],
        [      Plazas],
        [   Empleados]
    ])
    Inversa_A = inversa(Matriz_A)
    X         = Inversa_A*Matriz_B
    
    Imprimir(Residencia, Matriz_A, Matriz_B, Inversa_A, X)


Residencia_01 = Resolver("Residencia_01",65,110,10)
input()
Residencia_02 = Resolver("Residencia_02",50, 90, 8)
input()
Residencia_03 = Resolver("Residencia_03",75,130,12)
input()
Residencia_04 = Resolver("Residencia_04",90,170,15)