import os, random
os.system('cls')

def jugar():
    intentos = 0
    moneda = ["CARA", "SELLO"]
    while intentos < 3:
        lanzar = random.choice(moneda)
        elige = input("Cara o Sello? \n")
        eleccion = elige.upper()
        if lanzar == eleccion:
            print("Ganaste!")
            nuevosjuegos = input("¿Deseas jugar otra vez? -Si -No\n")
            nuevojuego = nuevosjuegos.upper()
            if nuevojuego == "SI":
                jugar()
            else:
                exit()
        else:
            intentos = intentos + 1
            total = 3 - intentos
            print("Te quedan ", total, " intentos")
            if intentos == 3:
                print("Perdiste")
                exit()

jugar()

        