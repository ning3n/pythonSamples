import os, random
os.system('cls')

def jugar():
    intentos = 0
    while intentos != 3:
        adivinanza = random.randint(0,10)
        alv = int(input("Numero del 1 al 9:\n"))
        if alv < 1 or alv > 9:
            print("Debes ingresar un numero entre el 1 y el 9")
            exit()
        elif alv == adivinanza:
            print("Ganaste!")
            nuevosjuegos=input("¿Deseas jugar otra vez? -Si  -No\n")
            nuevojuego = nuevosjuegos.upper()
            print("nuevojuego")
            if nuevojuego == "SI":
                jugar()
            else:
                exit()
        else:
            intentos = intentos + 1
            total = 3 - intentos
            print("Te quedan ", total, " intentos")
            if intentos == 3:
                print("Perdiste!")
                exit()

jugar()
