import os
os.system('cls')

fecha_evento = (2023, 9, 14)
print(type(fecha_evento)) 

print('El evento programado sera para la fecha:', fecha_evento)
print('El evento programado sera para la fecha: %i/%i/%i' % fecha_evento)

agno, mes, dia = fecha_evento
print('El evento programado sera para la fecha: {}/{}/{}'.format(agno,mes,dia))