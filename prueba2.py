from tkinter import *

# Crear la ventana principal
ventana = Tk()
ventana.title("Ejemplo de move()")
ventana.geometry("300x200")

# Crear el Canvas
canvas = Canvas(ventana, width=200, height=150, bg="white")
canvas.pack()

# Crear un rectángulo en el Canvas
rect_id = canvas.create_rectangle(50, 50, 100, 100, fill="blue")

# Función para mover el rectángulo
def mover_rectangulo():
    canvas.move(rect_id, 10, 0)  # Mover el rectángulo 10 unidades hacia la derecha y 0 unidades hacia abajo
    ventana.after(1000, mover_rectangulo)  # Programar el siguiente movimiento después de 1000 milisegundos (1 segundo)

# Iniciar el movimiento del rectángulo
mover_rectangulo()

# Ejecutar el bucle principal de la aplicación
ventana.mainloop()
