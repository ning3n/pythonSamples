import os

os.system('cls')

#-----------Solucion de Miwel-----------------------#
#numeros = input("Ingrese 3 numeros, separelos con comas \n")
#
#lista = []
#
#for caracter in numeros:
#    if caracter == ",":
#        pass
#    else:
#        lista.append(caracter)
#print(lista)
#-----------Solucion de Miwel-----------------------#
#-----------Solucion del profesor-------------------#
os.system('cls')

entrada = input("Ingrese numeros separados por coma: ")
numeros = entrada.split(',')
print(type(numeros))
print(numeros)
