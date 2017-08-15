
class Producto(object):
    def __init__(self,conf):
        self.codigo = conf[0]
        self.precio = conf[1]
    
    def getCodigo(self):
        return self.codigo

    def setCodigo(self,n):
        self.codigo=n

    def getPrecio(self):
        return self.precio
    
    def setPrecio(self,x):
        self.precio = x

