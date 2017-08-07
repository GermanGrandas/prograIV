
class Cd(object):
    def __init__(self,conf):
        self._tipo=conf[0]
        self._capacidad = conf[1]
        self._empty = True
        self._files = []
    
    def getTipo(self):
        return self._tipo
    #solo como prueba
    def setTipo(self,tipo):
        self._tipo = tipo
    
    def getCapacidad(self):
        return self._tipo
    
    def isEmpty(self):
        return self._empty

    def guardar(self,files):
        if self.isEmpty():
            for elemento in files:
                self._files.append(elemento)
            self._empty=False
        else:
            return False
    
    def __iter__(self):
        if not self.isEmpty():
            for elemento in self._files:
                yield elemento
        else:
            yield False
    def search(self):
        if not self.isEmpty():
            for x in self._files:
                print x

class Software(Cd):
    def __init__(self,conf):
        Cd.__init__(self,conf)
    
    def ejecutar(self):
        pass

class Audio(Cd):
    def __init__(self,conf):
        Cd.__init__(self,conf)
    
    def play(self):
        pass
    

class Docs(Cd):
    def __init__(self,conf):
        Cd.__init__(self,conf)
    
    def read(self):
        pass

    

