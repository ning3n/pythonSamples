import os, random
os.system('cls')

def juego():
    puntaje1 = 0
    puntajecpu = 0
    while puntaje1!=3 or puntajecpu!=3:
        opciones = ["piedra", "papel", "tijeras"]
        jugador1 = input("¿Piedra, Papel o Tijera? \n")
        cpu = random.choice(opciones)

        if (jugador1=="piedra" and cpu=="tijeras") or (jugador1=="tijeras" and cpu=="papel") or (jugador1=="papel" and cpu =="piedra"):
            print(cpu)
            puntaje1 = puntaje1+1
            print("Has ganado, puntaje: ", puntaje1)        
        elif jugador1==cpu:
            print("empate")
        else:
            print(cpu)
            puntajecpu=puntajecpu+1
            print("Ha ganado la cpu, puntaje: ", puntajecpu)

        if puntaje1 == 3:
            print("Has ganado!\n")
            nuevojuego=input("1-Nuevo Juego  2-Salir\n")
            if nuevojuego=="1" or nuevojuego=="Nuevo Juego":
                juego()
            else:
                exit()
                os.system('cls')

        if puntajecpu == 3:
            print("Has perdido!\n")
            nuevojuego=input("1-Nuevo Juego  2-Salir\n")
            if nuevojuego=="1" or nuevojuego=="Nuevo Juego":
                juego()
            else:
                exit()
                os.system('cls')            



nuevojuego=input("1-Nuevo Juego  2-Salir\n")

if nuevojuego=="1" or nuevojuego=="Nuevo Juego":
    juego()
else:
    exit()
    os.system('cls')