class Nodo:
    def __init__(self, nombre=None, cedula=None, izq=None, der=None):
        self.nombre = nombre
        self.cedula = cedula
        self.izq = izq
        self.der = der

    def __str__(self):
        return "%s %s" %(self.nombre, self.cedula)

class aBinarios:
    def __init__(self):
        self.raiz = None
    
    def agregar(self, elemento):
        if self.raiz == None:
            self.raiz = elemento
        else:
            aux = self.raiz
            padre = None
            while aux != None:
                padre = aux
                if int(elemento.cedula) >= int(aux.cedula):
                    aux = aux.der
                else:
                    aux = aux.izq
            if int(elemento.cedula) >= int (padre.cedula):
                padre.der = elemento
            else:
                padre.izq = elemento

    def preorden(self, elemento):
        if elemento != None:
            print(elemento)
            self.preorden(elemento.izq)
            self.preorden(elemento.der)   

    def postorden(self,elemento):
        if elemento != None:
            self.postorden(elemento.izq)
            self.postorden(elemento.der)
            print(elemento) 

    def inorden(self,elemento):
        if elemento != None:
            self.inorden(elemento.izq)
            print(elemento)
            self.inorden(elemento.der)

    def getRaiz(self):
        return self.raiz
               



if __name__ == "__main__":
    ab = aBinarios()
    while(True):
        print("---Menu---\n"+"1. Agregar\n"+"2.Preorden\n"+"3. PostOrden\n"+"4. Inorden")
        num = input("Ingrese la opcion")
        if num == "1":
            nombre = input("Ingrese nombre")
            cedula = input("Ingrese cedula")
            nod = Nodo(nombre, cedula)
            ab.agregar(nod)
        elif num =="2":
            print("Imprimiendo por Preorden")
            ab.preorden(ab.getRaiz())
        elif num == "3":
            print("Imprimiendo por PostOrden")
            ab.postorden(ab.getRaiz())
        elif num == "4":
            print("Imprimiendo por Inorden")
            ab.inorden(ab.getRaiz())

