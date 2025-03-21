import tkinter as tk
from tkinter import messagebox

def agregar_texto():
    texto = campo_texto.get()
    if texto:
        lista_textos.insert(tk.END, texto)
        campo_texto.delete(0, tk.END)

def limpiar_lista():
    lista_textos.delete(0, tk.END)

def mostrar_mensaje():
    print("Se va a mostrar un mensaje en la pantalla")
    messagebox.showinfo("Mensaje", "Hello, esto es un mensaje de prueba.")
    print("Se imprimió un mensaje en la pantalla")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Ejemplo de GUI con Tkinter")
ventana.geometry('400x400')

# Etiqueta para indicar qué hacer
etiqueta = tk.Label(ventana, text="Ingrese su texto:")
etiqueta.pack()

# Campo de texto para ingresar información
campo_texto = tk.Entry(ventana, width=40)
campo_texto.pack()

# Botón para agregar texto a la lista
boton_agregar = tk.Button(ventana, text="Agregar", command=agregar_texto)
boton_agregar.pack()

# Botón para mostrar mensaje
boton_mensaje = tk.Button(ventana, text="Mostrar mensaje", command=mostrar_mensaje)
boton_mensaje.pack()

# Botón para limpiar la lista
boton_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar_lista)
boton_limpiar.pack()

# Lista para mostrar los textos agregados
lista_textos = tk.Listbox(ventana, width=40)
lista_textos.pack()

# Ejecutar el bucle de eventos
ventana.mainloop()
