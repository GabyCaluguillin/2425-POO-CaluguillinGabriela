import tkinter as tk
from tkinter import messagebox

class ListaDeTareas:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tareas")
        self.root.geometry("400x400")

        # Crear la interfaz
        self.crear_interfaz()

        # Lista para almacenar las tareas
        self.tareas = []

    def crear_interfaz(self):
        # Frame principal
        main_frame = tk.Frame(self.root, padx=10, pady=10)
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Entrada de texto para nuevas tareas
        self.entry_tarea = tk.Entry(main_frame, width=30)
        self.entry_tarea.pack(pady=10)

        # Botón para añadir tarea
        boton_añadir = tk.Button(
            main_frame,
            text="Añadir Tarea",
            command=self.añadir_tarea
        )
        boton_añadir.pack(pady=5)

        # Lista de tareas (Listbox)
        self.listbox_tareas = tk.Listbox(
            main_frame,
            width=30,
            height=10,
            selectmode=tk.SINGLE
        )
        self.listbox_tareas.pack(pady=10)

        # Botón para marcar como completada
        boton_completar = tk.Button(
            main_frame,
            text="Marcar como Completada",
            command=self.marcar_completada
        )
        boton_completar.pack(pady=5)

        # Botón para eliminar tarea
        boton_eliminar = tk.Button(
            main_frame,
            text="Eliminar Tarea",
            command=self.eliminar_tarea
        )
        boton_eliminar.pack(pady=5)

        # Asociar la tecla Enter para añadir tarea
        self.entry_tarea.bind("<Return>", lambda event: self.añadir_tarea())

    def añadir_tarea(self):
        tarea = self.entry_tarea.get().strip()
        if tarea:
            # Añadir tarea a la lista y al Listbox
            self.tareas.append(tarea)
            self.listbox_tareas.insert(tk.END, tarea)
            self.entry_tarea.delete(0, tk.END)
        else:
            messagebox.showwarning("Entrada vacía", "Por favor, ingresa una tarea.")

    def marcar_completada(self):
        seleccion = self.listbox_tareas.curselection()
        if seleccion:
            tarea_index = seleccion[0]
            tarea_completada = self.tareas[tarea_index] + " (Completada)"
            # Actualizar la tarea en la lista y el Listbox
            self.tareas[tarea_index] = tarea_completada
            self.listbox_tareas.delete(tarea_index)
            self.listbox_tareas.insert(tarea_index, tarea_completada)
        else:
            messagebox.showwarning("Nada seleccionado", "Por favor, selecciona una tarea para marcar como completada.")

    def eliminar_tarea(self):
        seleccion = self.listbox_tareas.curselection()
        if seleccion:
            confirmar = messagebox.askyesno(
                "Eliminar Tarea",
                "¿Estás seguro de eliminar la tarea seleccionada?"
            )
            if confirmar:
                tarea_index = seleccion[0]
                # Eliminar la tarea de la lista y del Listbox
                self.tareas.pop(tarea_index)
                self.listbox_tareas.delete(tarea_index)
        else:
            messagebox.showwarning("Nada seleccionado", "Por favor, selecciona una tarea para eliminar.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ListaDeTareas(root)
    root.mainloop()
