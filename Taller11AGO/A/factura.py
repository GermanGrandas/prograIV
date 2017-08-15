
class Factura(object):
    def __init__(self):
        self.numero = 0
        self.productos = []

    def add(self,producto,cantidad):
        self.productos.append([producto,cantidad])
    
    def getNumero(self):
        return self.numero
    def setNumero(self,x):
        self.numero=x

    def getProductos(self):
        return self.productos

    def total(self):
        suma = 0
        for x in self.productos:
            suma+=x[0].precio*x[1]
        
        return suma

    def cambio(self,viejo,nuevo):
        i = 0
        for i in range(0,len(self.productos)):
            if self.productos[i][0] == viejo:
                self.productos[i][0] = nuevo[0]
                self.productos[i][1] = nuevo[1]
            i+=1
    
            



