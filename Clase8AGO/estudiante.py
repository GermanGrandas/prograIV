class Persona(object):
    def __init__(self, arg):
        self.edad = arg[0]
        self.cedula = arg[1]

    def getEdad(self):
        return self.edad

    def setEdad(self,edad):
        self.edad=edad

    def getCedula(self):
        return self.cedula

    def setCedula(self,cedula):
        self.cedula=cedula



class Estudiante(Persona):
    def __init__(self,arg):
        Persona.__init__(self,arg)
        self.notas = []
        self.n = None

    def setNotas(self,nota):
        if len(self.notas) != 3:
            self.notas.append(nota)
        else:
            pass

    def setN(self):
        suma
        for x in self.notas:
            suma+=x
        self.n=suma/(len(self.notas))
