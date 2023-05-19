from tkinter import *
import random

#variables globales
BASE = 460
ALTURA = 220
RADIO = 50

#funcion para modificar arco
def modificar_arco(angulo):
    c.itemconfig(arco, extent = angulo) 

#ventana principal
ventana_principal = Tk()
ventana_principal.title("David Fernando Muñoz Ortiz")
ventana_principal.geometry("500x500")
ventana_principal.resizable(0,0)
ventana_principal.config(bg="white")

#frame de graficacion
frame_grafica = Frame(ventana_principal)
frame_grafica.config(bg="green", width=480, height=240)
frame_grafica.place(x=10, y=10)

#creacion canvas
c = Canvas(frame_grafica, width=BASE, height=ALTURA)
c.config(bg="black")
c.place(x=10, y=10)

#arco
arco = c.create_arc(BASE/2 - RADIO, ALTURA/2 - RADIO, BASE/2 + RADIO, ALTURA/2 + RADIO, start = 0, extent = 0, fill = "blue")

#frame de controles
frame_controles = Frame(ventana_principal)
frame_controles.config(bg="green", width=480, height=230)
frame_controles.place(x=10, y=260)

#barra de desplazamiento
barra_desplazamiento = Scale(frame_controles, label="Angulo", from_=0, to=360, orient="horizontal", length=470, tickinterval=45, command=modificar_arco)
barra_desplazamiento.pack()

#desplegar ventana principal
ventana_principal.mainloop()