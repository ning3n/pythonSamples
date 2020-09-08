import os

os.system('cls')

cadena = "anitalavalatina"

cadena2 = ""

for i in range(len(cadena) -1, -1, -1):
    cadena2 += cadena[i]
    
print(cadena2)

#ALternativa de python
cadena3 = cadena[::-1]

if cadena == cadena2:
    print("Palindromo")
else:
    print("No es palindromo")