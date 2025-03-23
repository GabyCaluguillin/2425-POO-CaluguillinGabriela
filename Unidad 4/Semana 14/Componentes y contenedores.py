import tkinter as tk
from tkinter import messagebox, ttk
from tkcalendar import DateEntry  # Necesitarás instalar tkcalendar: pip install tkcalendar


# Función para agregar un evento a la lista
def agregar_evento():
    fecha = date_picker.get()
    hora = campo_hora.get()
    descripcion = campo_descripcion.get()

    if fecha and hora and descripcion:
        # Agregar el evento al TreeView
        treeview.insert("", tk.END, values=(fecha, hora, descripcion))
        # Limpiar los campos de entrada
        campo_hora.delete(0, tk.END)
        campo_descripcion.delete(0, tk.END)
    else:
        messagebox.showwarning("Campos vacíos", "Por favor, complete todos los campos.")


# Función para eliminar un evento seleccionado
def eliminar_evento():
    seleccionado = treeview.selection()
    if seleccionado:
        # Confirmar eliminación
        confirmar = messagebox.askyesno("Eliminar Evento", "¿Está seguro de eliminar el evento seleccionado?")
        if confirmar:
            treeview.delete(seleccionado)
    else:
        messagebox.showwarning("Nada seleccionado", "Por favor, seleccione un evento para eliminar.")


# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Agenda Personal")
ventana.geometry('600x400')

# Frame para la entrada de datos
frame_entrada = tk.Frame(ventana)
frame_entrada.pack(pady=10)

# Etiquetas y campos para la fecha, hora y descripción
tk.Label(frame_entrada, text="Fecha:").grid(row=0, column=0, padx=5, pady=5)
date_picker = DateEntry(frame_entrada, width=12, background='darkblue', foreground='white', borderwidth=2)
date_picker.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_entrada, text="Hora:").grid(row=0, column=2, padx=5, pady=5)
campo_hora = tk.Entry(frame_entrada, width=10)
campo_hora.grid(row=0, column=3, padx=5, pady=5)

tk.Label(frame_entrada, text="Descripción:").grid(row=0, column=4, padx=5, pady=5)
campo_descripcion = tk.Entry(frame_entrada, width=30)
campo_descripcion.grid(row=0, column=5, padx=5, pady=5)

# Frame para los botones de acción
frame_botones = tk.Frame(ventana)
frame_botones.pack(pady=10)

# Botones para agregar, eliminar y salir
boton_agregar = tk.Button(frame_botones, text="Agregar Evento", command=agregar_evento)
boton_agregar.grid(row=0, column=0, padx=5)

boton_eliminar = tk.Button(frame_botones, text="Eliminar Evento", command=eliminar_evento)
boton_eliminar.grid(row=0, column=1, padx=5)

boton_salir = tk.Button(frame_botones, text="Salir", command=ventana.quit)
boton_salir.grid(row=0, column=2, padx=5)

# Frame para la lista de eventos (TreeView)
frame_lista = tk.Frame(ventana)
frame_lista.pack(pady=10)

# Crear el TreeView para mostrar los eventos
columnas = ("Fecha", "Hora", "Descripción")
treeview = ttk.Treeview(frame_lista, columns=columnas, show="headings", selectmode="browse")

# Configurar las columnas del TreeView
for col in columnas:
    treeview.heading(col, text=col)
    treeview.column(col, width=150)

treeview.pack()

# Ejecutar el bucle de eventos
ventana.mainloop()
