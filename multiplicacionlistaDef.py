lista = [3,2,1]

def calculo(lista):
    lista_nueva = []

    for i in range (0, len(lista)):
        lista_original = lista
        entero_original = lista_original[i]
        lista_original[i] = 1

        resultado = 1

        for x in lista_original:
            resultado = resultado * x
            print(resultado)
        
        lista_nueva.append(resultado)

        lista_original[i] = entero_original
    
    return lista_nueva

r = calculo(lista)
print(r)