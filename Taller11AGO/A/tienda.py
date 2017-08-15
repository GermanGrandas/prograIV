from factura import *
from producto import *


class Tienda(object):
    def __init__(self):
        self.productos=[]
        self.facturas=[]
        self.cont = 0

    def addProduct(self,product):
         p = Producto(product)
         self.productos.append(p)
    
    def getProduct(self):
        return self.productos

    def newBill(self):
        f = Factura()
        f.setNumero(self.cont)
        x = self.cont
        self.cont+=1
        self.facturas.append(f)
        return x

    def searchProduct(self,product):
        for x in self.productos:
            if x.codigo == product:
                return True
        else:
            return False

    def addProductToBill(self,numero,producto,cantidad):
        for bill in self.facturas:
                if numero == bill.numero and self.searchProduct(producto):
                    for product in self.productos:
                        if product.codigo == producto:
                            bill.add(product,cantidad)
    

    def getBill(self,number):
        for x in self.facturas:
            if x.numero==number:
                return x

    

if __name__ == '__main__':
    newt = Tienda()
    newt.addProduct([0,34.5])
    newt.addProduct([1,0.98])
    newt.addProduct([2,1])

    ref = newt.newBill()
    newt.addProductToBill(ref,0,3)
    newt.addProductToBill(ref,1,3)

    fact = newt.getBill(ref).total()

    ref2 = newt.newBill()
    newt.addProductToBill(ref2,0,10)
    newt.addProductToBill(ref2,2,56)

    fact2 = newt.getBill(ref2).total()

    print str(fact) + " " +str(fact2)


