
class Producto:
    def __init__(self, lista, listaProducto):
        self.lista = lista
        self.listaProducto = listaProducto

    def resultante(self, lista, listaProducto):
        contadorL = 0
        for i in lista:
            for j in lista:
                if contadorL == 0:
                    resultado = i*j
                elif contadorL == 1:
                    resultado = resultado * j
                else:
                    resultado = resultado * resultado
                print(resultado)

                if contadorL == len(lista):
                    listaProducto.append(resultado)
            
            contadorL = contadorL + 1      

        return listaProducto  
            

lista = [1,2,3,4,5]
listaProducto = []

resultado = Producto(lista, listaProducto)

print(resultado.resultante(lista, listaProducto))
                


