from estudiante import *


if __name__ == '__main__':
    lista=[]
    while len(lista) < 3:
        cedula = input("Ingrese la cedula del estudiante:")
        edad = input("Ingrese la edad del estudiante: ")
        estudiante = Estudiante([edad,cedula])
        i=0
        while i<3:
            nota = input("Ingrese la nota "+str(i+1)+": ")
            estudiante.setNotas(nota)
            estudiante.setN()
            i+=1
        print "---------------------"
        i=0
        lista.append(estudiante)
    print lista
