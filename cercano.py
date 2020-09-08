import os
os.system('cls')

def cercania(n):
    """
        Comprueba si un numero es cercano a 1000 o 2000 usando valor absoluto
    """
    return (abs(1000 - n) < 100) or (abs(2000-n) < 100)

print(cercania(1000))
print(cercania(950))
print(cercania(200))

print()

print(cercania(2000))
print(cercania(1950))
print(cercania(3200))