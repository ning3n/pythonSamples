import os, random
os.system('cls')

def jugar():
    intentos = 0
    oro = 0

    while intentos < 3:
        tipoDragon=["TRANQUILO", "ASESINO"]
        dragonquetoca = random.choice(tipoDragon)
        cuevaIzquierda = dragonquetoca
        cuevaDerecha = dragonquetoca
        cuevaMedio = dragonquetoca
        juegos = input("Estas en el reino dragon, tienes 3 cuevas en frente. Una a la izquierda, una a la derecha y una en el medio... En cualquiera de las tres puede haber un dragon tranquilo o uno asesino ¿Cuál eliges?\n")
        juego = juegos.upper()
        if juego == "IZQUIERDA":
            if cuevaIzquierda == "ASESINO":
                print("El dragon te devora, ¡has perdido! acumulaste: ", oro, " de oro")
                intentos = intentos + 1
                oro = 0
            else:
                totaloro = random.randint(200,500)
                oro = oro + totaloro
                print("El dragon es amigable con los humanos y te entrega: ", totaloro, " de oro, felicidades")
                print("Tienes en total: ", oro)
        elif juego == "DERECHA":
            if cuevaDerecha == "ASESINO":
                print("El dragon te devora, ¡has perdido! acumulaste: ", oro, " de oro")
                intentos = intentos + 1
                oro = 0
            else:
                totaloro = random.randint(200,500)
                oro = oro + totaloro
                print("El dragon es amigable con los humanos y te entrega: ", totaloro, " de oro, felicidades")
                print("Tienes en total: ", oro)
        elif juego == "MEDIO":
            if cuevaMedio == "ASESINO":
                print("El dragon te devora, ¡has perdido! acumulaste: ", oro, " de oro")
                intentos = intentos + 1
                oro = 0
            else:
                totaloro = random.randint(200,500)
                oro = oro + totaloro
                print("El dragon es amigable con los humanos y te entrega: ", totaloro, " de oro, felicidades")
                print("Tienes en total: ", oro)        
        else:
            print("Debes elegir una opcion valida")

        if intentos == 3:
            print("¡Has perdido! total de oro acumulado: ", oro)
            nuevosjuegos=input("¿Deseas jugar otra vez? -Si  -No\n")
            nuevojuego = nuevosjuegos.upper()
            if nuevojuego == "SI":
                jugar()
            else:
                exit()

jugar()

