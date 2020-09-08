import os
os.system('cls')

def caracteres(cadena):
    if isinstance(cadena, str):
        print(len(cadena))
        alv = input("Deseas insertar otra cadena? -Si  -No\n")
        alv2 = alv.upper()
        if alv2 == "SI":
            palabra = input("Ingresa la cadena a contar: \n")
            print(caracteres(palabra))
        else:
            exit()
    else:
        print("Debes ingresar una cadena")
        palabra = input("Ingresa la cadena a contar: \n")
        print(caracteres(palabra))


palabra = input("Ingresa la cadena a contar: \n")
print(caracteres(palabra))
