from tkinter import *
import random

#variables globales
BASE = 460
ALTURA = 220

#ventana principal
ventana_principal = Tk()

ventana_principal.title("David Fernando Muñoz Ortiz")
ventana_principal.geometry("500x500")
ventana_principal.resizable(0,0)
ventana_principal.config(bg="white")

#frame
frame_grafica = Frame(ventana_principal)
frame_grafica.config(bg="green", width=480, height=240)
frame_grafica.place(x=10, y=10)

#creacion canvas
c = Canvas(frame_grafica, width=BASE, height=ALTURA)
c.config(bg="black")
c.place(x=10, y=10)

#graficación
for i in range(100):
    x = random.randint(0, BASE - 20)
    y = random.randint(0, ALTURA - 20)
    color = "#"
    for k in range(6):
        color = color + random.choice("0123456789ABCDEF")
    circulo = c.create_oval(x,y,x + 20,y + 20, fill=color)


#desplegar ventana principal
ventana_principal.mainloop()