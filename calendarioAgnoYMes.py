import os
os.system('cls')

import calendar

agno = int(input("¿Que año?: \n"))
mes = int(input("¿Que mes?:  \n"))

print(calendar.month(agno, mes))