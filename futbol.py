from tkinter import *

# Dimensiones del lienzo
ANCHO = 640
ALTO = 420

# Variables de la bola
radio = 30
x = ANCHO / 2
y = ALTO / 2
velocidad_x = 3
velocidad_y = 3

# Función para mover la bola y controlar el rebote
def mover_bola():
    global x, y, velocidad_x, velocidad_y
    
    # Actualizar la posición de la bola
    x += velocidad_x
    y += velocidad_y
    
    # Verificar los límites del lienzo y controlar el rebote
    if x <= radio or x >= ANCHO - radio:
        velocidad_x = -velocidad_x
    if y <= radio or y >= ALTO - radio:
        velocidad_y = -velocidad_y
    
    # Mover la bola en el lienzo
    canvas.move(bola, velocidad_x, velocidad_y)
    
    # Llamar a la función de forma recursiva después de un intervalo de tiempo
    canvas.after(30, mover_bola)

# Función para iniciar el movimiento de la bola
def iniciar_movimiento():
    mover_bola()
# Crear la ventana principal
ventana = Tk()
ventana.title("Simulación de mesa de billar")
ventana.resizable(0, 0)


# Crear el lienzo
canvas = Canvas(ventana, width=ANCHO, height=ALTO, bg="green")
canvas.pack()

# Cargar la imagen de la cancha
imagen_fondo = PhotoImage(file="cancha.png")

# Mostrar la imagen de la cancha en el lienzo
canvas.create_image(0, 0, anchor=NW, image=imagen_fondo)

# Cargar la imagen de la bola
imagen_bola = PhotoImage(file="balon.png")

# Crear la bola en el lienzo utilizando la imagen
bola = canvas.create_image(x, y, image=imagen_bola)

# Crear el botón para iniciar el movimiento
boton_inicio = Button(ventana, text="Iniciar", command=iniciar_movimiento)
boton_inicio.pack()

# Ejecutar el bucle principal de la ventana
ventana.mainloop()
