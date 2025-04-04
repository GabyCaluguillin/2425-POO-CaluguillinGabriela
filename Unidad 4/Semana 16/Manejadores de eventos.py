import tkinter as tk
from tkinter import messagebox

# Lista de tareas
tasks = []

def update_task_list():
    # Limpia la lista de tareas visualmente
    listbox.delete(0, tk.END)
    # Muestra las tareas en la lista
    for task in tasks:
        listbox.insert(tk.END, task)

def add_task():
    task = text_entry.get()  # Obtiene el texto de la entrada
    if task:
        tasks.append(f"{task} - Pendiente")  # Añade la tarea con el estado pendiente
        text_entry.delete(0, tk.END)  # Limpia el campo de entrada
        update_task_list()  # Actualiza la lista

def mark_task_completed():
    try:
        # Obtiene la tarea seleccionada
        selected_task_index = listbox.curselection()[0]
        task = tasks[selected_task_index]
        if "- Completada" not in task:  # Marca la tarea como completada si no lo está
            tasks[selected_task_index] = task.replace("- Pendiente", "- Completada")
            update_task_list()
    except IndexError:
        messagebox.showwarning("Advertencia", "Por favor, selecciona una tarea.")

def delete_task():
    try:
        # Obtiene la tarea seleccionada
        selected_task_index = listbox.curselection()[0]
        tasks.pop(selected_task_index)  # Elimina la tarea de la lista
        update_task_list()  # Actualiza la lista
    except IndexError:
        messagebox.showwarning("Advertencia", "Por favor, selecciona una tarea.")

def on_enter_key(event):
    add_task()

def on_escape_key(event):
    root.quit()

def on_c_key(event):
    mark_task_completed()

def on_d_key(event):
    delete_task()

root = tk.Tk()
root.title("Gestión de Tareas")
root.geometry("400x400")  # Establece un tamaño para la ventana

# Instrucciones
instruction_label = tk.Label(root, text="Por favor, ingresa una tarea:", font=("Arial", 14))
instruction_label.pack(pady=(10, 0))

# Entrada de texto
text_entry = tk.Entry(root, font=("Arial", 14))
text_entry.pack(pady=10)

# Botón para añadir tarea
add_button = tk.Button(root, text="Añadir tarea", command=add_task)
add_button.pack(pady=(0, 10))

# Lista de tareas
listbox = tk.Listbox(root, font=("Arial", 12), selectmode=tk.SINGLE, height=10)
listbox.pack(pady=10)

# Funciones de atajos de teclado
root.bind('<Return>', on_enter_key)  # Tecla Enter para añadir tarea
root.bind('<Escape>', on_escape_key)  # Tecla Escape para cerrar
root.bind('<c>', on_c_key)  # Tecla 'C' para marcar tarea como completada
root.bind('<d>', on_d_key)  # Tecla 'D' para eliminar tarea

# Pone el foco en la entrada de texto para que el usuario pueda escribir inmediatamente
text_entry.focus_set()

root.mainloop()
