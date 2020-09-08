import datetime
import os

os.system('cls')

ahora = datetime.datetime.now()

print(ahora)

print(type(ahora))

print(ahora.strftime('%d/%m/%Y %H:%M:%S'))