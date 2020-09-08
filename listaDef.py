lista = [8, 11, 2, 7]
k = 9
cantidad = len(lista)

def calculoLista (lista, k):
    for i in range (cantidad):
        cantidad_l = len(lista)
        numeroBase = lista[0]
        sumatoria = 0

        lista.pop(0)

        cantidad_l = len(lista)

        for j in range (cantidad_l):
            sumatoria = numeroBase + lista[j]

            if sumatoria == k:
                return numeroBase, lista[j]
    
    return False

r = calculoLista(lista,k)

if r:
    print(f'Hubo una coincidencia con k({k}), {r[0]} + {r[1]}')
else:
    print("No hubo coincidencia")
