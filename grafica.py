from tkinter import *

#variables globales
BASE = 460
ALTURA = 220

#ventana principal
ventana_principal = Tk()

ventana_principal.title("David Fernando Muñoz Ortiz")
ventana_principal.geometry("500x500")
ventana_principal.resizable(0,0)
ventana_principal.config(bg="medium aquamarine")

#frame
frame_grafica = Frame(ventana_principal)
frame_grafica.config(bg="aquamarine2", width=480, height=240)
frame_grafica.place(x=10, y=10)

#creacion canvas
c = Canvas(frame_grafica, width=BASE, height=ALTURA)
c.place(x=10, y=10)

"""#lineas
linea1 = c.create_line(10,10, BASE - 10, 10, fill="red")
linea2 = c.create_line(BASE - 10, 10, BASE - 10, ALTURA - 10, fill="red")
linea3 = c.create_line(BASE - 10, ALTURA - 10, 10, ALTURA -10, fill="red")
linea4 = c.create_line(10, ALTURA -10, 10, 10, fill="red")
linea5 = c.create_line(10, 10, BASE - 10, ALTURA - 10, fill="blue")
linea6 = c.create_line(10, ALTURA -10, BASE - 10, 10, fill="black")

#cruz
linea7 = c.create_line(BASE/2 - 20,ALTURA/2 -60,BASE/2 + 20,ALTURA/2 -60, fill="red")
linea8 = c.create_line(BASE/2 + 20,ALTURA/2 -60,BASE/2 + 20,ALTURA/2 -20, fill="red")
linea9 = c.create_line(BASE/2 + 20,ALTURA/2 -20,BASE/2 + 60,ALTURA/2 -20, fill="red")
linea10 = c.create_line(BASE/2 + 60,ALTURA/2 -20,BASE/2 + 60,ALTURA/2 +20, fill="red")
linea11 = c.create_line(BASE/2 + 60,ALTURA/2 +20,BASE/2 + 20,ALTURA/2 +20, fill="red")
linea12 = c.create_line(BASE/2 + 20,ALTURA/2 -20,BASE/2 + 60,ALTURA/2 -20, fill="red")
linea13 = c.create_line(220,100,260,100, fill="red")
linea14 = c.create_line(220,100,260,100, fill="red")
linea15 = c.create_line(220,100,260,100, fill="red")
linea16 = c.create_line(220,100,260,100, fill="red")
linea17 = c.create_line(220,100,260,100, fill="red")
linea18 = c.create_line(220,100,260,100, fill="red")"""

#
#texto1 = c.create_text(BASE/2, ALTURA/2, text="Sitemas UIS Socorro", anchor="center", font=("Arial", "20", "bold"), fill="green", activefill="blue")

#cuadradros y rectangulos
"""rect1 = c.create_rectangle(20, 20, 120, 120, fill="pink", outline="red", width="5")"""

#poligonos
"""poligono1 = c.create_polygon(0,0,BASE/2,ALTURA/2,BASE,ALTURA, fill="red", outline="red")
poligono2 = c.create_polygon(0,ALTURA,BASE/2,ALTURA/2,BASE,ALTURA, fill="green", outline="red")"""
poligono1 = c.create_polygon((BASE/2)/2,0,BASE/2,(ALTURA/2)/2,(BASE/2)/2,ALTURA/2,0,(ALTURA/2)/2, fill="red", outline="red")
poligono1 = c.create_polygon((BASE/2)*1.5,0,BASE,(ALTURA/2)/2,(BASE/2)*1.5,ALTURA/2,BASE/2,(ALTURA/2)/2, fill="blue", outline="red")
poligono1 = c.create_polygon((BASE/2)/2,ALTURA/2,BASE/2,(ALTURA/2)*1.5,(BASE/2)/2,ALTURA,0,(ALTURA/2)*1.5, fill="green", outline="red")
poligono1 = c.create_polygon((BASE/2)*1.5,ALTURA/2,BASE,(ALTURA/2)*1.5,(BASE/2)*1.5,ALTURA,BASE/2,(ALTURA/2)*1.5, fill="black", outline="red")

#pacman
pacman = c.create_arc((BASE/4)-30, (ALTURA/4)-30,(BASE/4)+30, (ALTURA/4)+30, start=45, extent=280, fill="yellow" )
ojo = c.create_oval((BASE/4)-5, (ALTURA/4)-15,(BASE/4)+-1, (ALTURA/4)-12, fill="black" )
pacman = c.create_arc((BASE/2)*1.5-30, (ALTURA/4)-30,(BASE/2)*1.5+30, (ALTURA/4)+30, start=45, extent=280, fill="yellow" )

pacman = c.create_arc((BASE/4)-30, (ALTURA/2)*1.5-30, (BASE/4)+30, (ALTURA/2)*1.5+30, start=45, extent=280, fill="yellow" )

pacman = c.create_arc((BASE/2)*1.5-30, (ALTURA/2)*1.5-30,(BASE/2)*1.5+30, (ALTURA/2)*1.5+30, start=45, extent=280, fill="yellow" )

"""#ovalos y circulo
elipse1 = c.create_oval(BASE/2,ALTURA/2,BASE,ALTURA, fill="orange")
elipse1 = c.create_oval((BASE/2)-50,(ALTURA/2)-50,(BASE/2)+50,(ALTURA/2)+50, fill="orange")

#arcos
arc1 =c.create_arc((BASE/2)-30,(ALTURA/2)-30,(BASE/2)+30,(ALTURA/2)+30, start=45,extent=45, fill="black")
arc1 =c.create_arc((BASE/2)-30,(ALTURA/2)-30,(BASE/2)+30,(ALTURA/2)+30, start=45,extent=45, fill="black")"""


#desplegar ventana principal
ventana_principal.mainloop()