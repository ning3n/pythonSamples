import os 
os.system('cls')
from math import pi

r = float(input("Ingrese el valor del radio: \n"))

volumen = (4/3)*pi*(r**3)
print('El volumen de la esfera es {} unidades cúbicas'.format(volumen))