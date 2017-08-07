class Producto(object):
    def __init__(self,values):
        self._price = values[0]
        self._id = values[1]
    
    def getPrice(self):
        return self._price

    def setPrice(self,value):
        self._price = value

    def getId(self):
        return self._id
    
class Micro(Producto):
    def __init__(self,values):
        Producto.__init__(self,[values[0],values[1]])
        self.voltaje = values[2]

class Resistencia(Producto):
    def __init__(self,values):
        Producto.__init__(self,[values[0],values[1]])
        self.resvalue = values[2]


    