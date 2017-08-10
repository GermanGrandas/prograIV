#!/usr/bin/env python
#-*- coding: utf-8 -*-
from estudiante import *
from Tkinter import *


raiz = Tk()
raiz.geometry('300x300+500+50')
raiz.title("Estudiantes")
lista = []


def addEntry():
    estudiante = Estudiante([edadVar.get(),idVar.get(),nameVar.get()])
    estudiante.setNotas([nota1Var.get(),nota2Var.get(),nota3Var.get()])
    lista.append(estudiante)
    
    #lista.append([edadVar.get(),idVar.get(),nameVar.get()])
    newv.destroy()
    raiz.deiconify()
    update(raiz)
    #setSelect ()

def newStudent():
    global newv ,edadVar , idVar,nameVar , nota1Var,nota2Var,nota3Var
    newv = Toplevel(raiz)
    newv.geometry('300x300+500+50')
    #Labels para añadir información 

    frame1 = Frame(newv)
    frame1.pack()

    Label(frame1, text="Nombre").grid(row=0, column=0, sticky=W)
    nameVar = StringVar()
    name = Entry(frame1, textvariable=nameVar)
    name.grid(row=0, column=1, sticky=W)

    Label(frame1, text="Cedula").grid(row=1, column=0, sticky=W)
    idVar= IntVar(value=0)
    idC= Entry(frame1, textvariable=idVar)
    idC.grid(row=1, column=1, sticky=W)

    Label(frame1, text="Edad").grid(row=2, column=0, sticky=W)
    edadVar= IntVar(value=0)
    edad= Entry(frame1, textvariable=edadVar)
    edad.grid(row=2, column=1, sticky=W)

    Label(frame1, text="Notas").grid(row=3, column=1, sticky=W)

    Label(frame1, text="Nota 1").grid(row=4, column=0, sticky=W)
    nota1Var= DoubleVar(value=0) 
    nota1= Entry(frame1, textvariable=nota1Var)
    nota1.grid(row=4, column=1, sticky=W)

    Label(frame1, text="Nota 2").grid(row=5, column=0, sticky=W)
    nota2Var= DoubleVar(value=0) 
    nota2= Entry(frame1, textvariable=nota2Var)
    nota2.grid(row=5, column=1, sticky=W)

    Label(frame1, text="Nota 3").grid(row=6, column=0, sticky=W)
    nota3Var= DoubleVar(value=0) 
    nota3= Entry(frame1, textvariable=nota3Var)
    nota3.grid(row=6, column=1, sticky=W)

   
        
    #Botón de Ok
    frame2 = Frame(newv)       # Row of buttons
    frame2.pack()
    b1 = Button(frame2,text=" Ok  ",command=addEntry)
    b1.pack(side=LEFT)
    raiz.iconify()

def config(raiz):
    global select
    menubarra = Menu(raiz)
    menubarra.add_command(label="Añadir", command=newStudent)
    menubarra.add_command(label="Salir", command=raiz.quit)
    # Mostrar el menu
    raiz.config(menu=menubarra)

    frame1 = Frame(raiz)
    frame1.pack()
    Label(frame1, text="Nombre").grid(row=0, column=0, sticky=W ,padx=10, pady=15)
    Label(frame1, text="Notas").grid(row=0, column=2, sticky=W,padx=10, pady=15)
    Label(frame1, text="Promedio").grid(row=0, column=3, sticky=W,padx=10, pady=15)


    frame2 = Frame(raiz)
    frame2.pack()
    scroll = Scrollbar(frame2, orient=VERTICAL)

    select = Listbox(frame2, yscrollcommand=scroll.set, height=100 , width = 200)
    scroll.config (command=select.yview)
    scroll.pack(side=RIGHT, fill=Y)
    select.pack(side=LEFT,  fill=BOTH, expand=1)
    

def update(root):
    lista.sort()
    select.delete(0, END)
    for estudiantes in lista:
        cad = estudiantes.nombre+"     "+str(estudiantes.notas[0]) +"   "+str(estudiantes.notas[1])+"    "+str(estudiantes.notas[2]) +"     "+str(estudiantes.n)
        select.insert('end',cad)
        


# Mostrar la ventana
config(raiz)
raiz.mainloop()