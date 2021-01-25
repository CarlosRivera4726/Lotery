import random
from tkinter import *
from tkinter import messagebox
from os import system
import os

if __name__ == '__main__':
    def participantes(numero):
        txtBox["state"]="disabled"
        try:
            numParticipantes = int(numero)
            lista = []
            for x in range(0,numParticipantes):
                lista.append(input(f"Ingresa el nombre del participante número {x+1}: "))
            
            numRandom = random.randrange(numParticipantes)
            participantes = lista[numRandom]
            ganador = str(participantes)
            nameOs = os.name
            messagebox.showwarning("Winner",f"el participante ganador es: {ganador}")
        except ValueError as numero:
            messagebox.showwarning("Warning","Recuerda colocar el número de participantes")
        except RuntimeError as lista:
            messagebox.showwarning("Warning","has presionado muchas veces el botón de número de participantes!, completa primero la anterior!")
    ####función para habilitar el txtBox y limpiar la consola
    def habilitar():
        txtBox["state"]="normal"
        if os.name == "nt":
            system("cls")
        else:
            system("clear")

    gui = Tk()
    gui.title("Sorteo!!!!!!!")
    ######logic#####
    '''
    numParticipantes = int(input("Ingrese el número de participantes: "))
    lista = participantes(numParticipantes)
    numeroRandom = random.randrange(numParticipantes)
    print(f"Ganador {lista[numeroRandom]}")
    
    def participantes(numParticipantes):
        lista=[]
        lista.append(input("ingrese el nombre de los participantes: ")
        #print(lista)
        return lista
    '''
    ######gui########
    lbl1 = Label(gui,text="número de participantes: ")
    lbl2 = Label(gui, text="El participante ganador es: ")

    addPart = Button(gui, text="número de participantes", command=lambda:participantes(txtBox.get()))
    ####Botón para habilitar el txtBox
    Button(gui, text="Habilitar", command=lambda:habilitar()).grid(row=6,column=1)
    txtBox = Entry(gui)
    ####botón para salir####
    Button(gui, text="salir", command=lambda:exit()).grid(row=6, column=0)
    ####grillas####
    lbl1.grid(row=5, column=1)
    txtBox.grid(row=5, column=3)
    addPart.grid(row=6,column=3)
    gui.mainloop()
