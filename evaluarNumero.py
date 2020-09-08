import os
os.system('cls')

def operacion(numero):
    resultado = numero + numero
    return resultado

numero = int(input("Ingrese un número: \n"))

print("El resultado de la operación es: ", operacion(numero))

##------------------------------------------------------------

def diferencia(numero):
    if numero <= 15:
        return 15-numero
    else:
        return (15-numero)*2

print("")
print("El segundo resultado es: ", diferencia(numero))