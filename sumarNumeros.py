import os
os.system('cls')

def sumar_numeros(a,b,c):
    """
        Calcula la suma de 3 numeros, si son iguales, la suma se multiplica por 3.
    """
    
    suma = a + b + c

    if a == b and a == c:
        suma *= 3

    return suma

print(sumar_numeros(2,2,7))