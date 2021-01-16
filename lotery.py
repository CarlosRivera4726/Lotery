import random
from tkinter import *
from os import system
import os
import ctypes  # An included library with Python install. 
if __name__ == '__main__':
    def participantes(numero):
        txtBox["state"]="disabled"
        try:
            numParticipantes = int(numero)
            lista = []
            for x in range(0,numParticipantes):
                lista.append(input(f"Ingresa el nombre del participante número {x+1}: "))
            
            numRandom = random.randrange(numParticipantes)
            ganador = lista[numRandom]
            ganado = str(ganador)
            ctypes.windll.user32.MessageBoxW(0,f"el participante número {numRandom+1} es: {ganado}","Winner",1)
        except ValueError as numero:
            ctypes.windll.user32.MessageBoxW(0,"Recuerda colocar el número de participantes","Warning",1)
        except RuntimeError as lista:
            ctypes.windll.user32.MessageBoxW(0,"has presionado muchas veces el botón de número de participantes!, completa primero la anterior!","Warning",1)
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
    print(lista[numeroRandom])
    '''
    ######gui########
    lbl1 = Label(gui,text="número de participantes: ")
    lbl2 = Label(gui, text="El participante ganador es: ")

    addPart = Button(gui, text="número de participantes", command=lambda:participantes(txtBox.get()))
    ####Botón para habilitar el txtBox
    Button(gui, text="Habilitar", command=lambda:habilitar()).grid(row=6,column=1)
    txtBox = Entry(gui)
    ####grillas####
    lbl1.grid(row=5, column=1)
    txtBox.grid(row=5, column=3)
    addPart.grid(row=6,column=3)
    gui.mainloop()