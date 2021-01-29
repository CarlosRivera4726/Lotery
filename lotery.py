import random
from tkinter import *
from tkinter import messagebox
from os import system
import os
def participantes(numero):
        txtBox["state"]="disabled"
        try:
            numeroParticipantes = int(numero)
            lista = []
            for x in range(0,numeroParticipantes):
                nombreParticipante = input(f"Ingresa el nombre del participante número {x+1}: ")
                if len(nombreParticipante) != 0:
                    lista.append(nombreParticipante)
                else:
                    nombreParticipante = input(f"Ingresa el nombre del participante número {x+1}: ")
                    if len(nombreParticipante) == 0:
                        break
                    else:
                      lista.append(nombreParticipante)  

            numeroRandom = random.randrange(numeroParticipantes)
            participantes = lista[numRandom]
            ganador = str(participantes)

            messagebox.showinfo("Winner",f"el participante ganador es: \n\n\t{numeroRandom+1}) {ganador}")
        except ValueError as numero:
            messagebox.showwarning("Warning","Recuerda colocar el número de participantes")
        except RuntimeError as lista:
            messagebox.showwarning("Warning","has presionado el botón de agregar numero de participantes repetidas veces, debes terminar el programa anterior")
        except IndexError as lista:
            messagebox.showwarning("ERROR!!!!","No has ingresado ningún nombre y la lista no pudo continuar")        
def habilitar():
        txtBox["state"]="normal"
        if os.name == "nt":
            system("cls")
        else:
            system("clear")

if __name__ == '__main__':        
    ####función para habilitar el txtBox y limpiar la consola

    gui = Tk()
    gui.title("Sorteo!!!!!!!")
    messagebox.showinfo("Datos claros!","RECUERDA QUE EL NOMBRE INGRESADO, DEBE SER MAYOR DE 3 CARACTERES!")  
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
