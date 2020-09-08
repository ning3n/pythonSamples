import os
os.system('cls')

nombre_archivo = input('ingrese el nombre del archivo: \n')

parte_nombre_archivo = nombre_archivo.split('.')

print(parte_nombre_archivo)

print(" La extension del archivo es:", parte_nombre_archivo[-1])