class Persona:
    # método constructor de la clase persona
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre      #guarda el nombre de la persona
        self.apellido = apellido    #guarda el apellido de la persona
        self.edad = edad     #guarda la edad de la persona
        print(f"se ha creado una persona. Método constructor ejecutado.")

        # Métodos personalizados
    def informacion(self):
        print(f"persona: {self.nombre}, {self.apellido}, {self.edad} años.")

# método destructor se ejecuta automaticamente cuando el objeto es eliminado

    # Método destructor
    def __del__(self):
        print("Método destructor ejecutado.")

# Creación del objeto / Instancia de la clase
persona = Persona('Leo', 'Cacuango', '30')
persona.informacion()


