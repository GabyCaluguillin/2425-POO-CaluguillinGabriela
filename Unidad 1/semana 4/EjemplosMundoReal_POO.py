class Libro:
# Inicializa los atributos del libro
    def __init__(self, título, autor, isbn):
        self.título = título
        self.autor = autor
        self.isbn = isbn
        self.is_borrowed = False
#Cambia el estado del libro a prestado si aún no lo está
    def prestar(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            return True
        return False

#Este método cambia el estado del libro a disponible

    def devolver(self):
        self.is_borrowed = False
#Define cómo se representa un objeto Libro cuando se imprime. Devuelve una cadena con la información del libro
    def __str__(self):
        return f"{self.título} por {self.autor}, ISBN: {self.isbn}"
#Inicializa un nuevo bibliotecario con un nombre
class Bibliotecario:
    def __init__(self, nombre):
        self.nombre = nombre
#Gestiona las acciones de prestar y devolver libros. Llama al método correspondiente del libro según la acción indicada
    def gestionar_libro(self, libro, accion):
        if accion == 'prestar':
            return libro.prestar()
        elif accion == 'devolver':
            libro.devolver()

class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros_prestados = []
#Este método permite al usuario pedir prestado un libro
    def pedir_prestado(self, libro, bibliotecario):
        if bibliotecario.gestionar_libro(libro, 'prestar'):
            self.libros_prestados.append(libro)
            print(f"{self.nombre} ha pedido prestado el libro: {libro.título}")
        else:
            print(f"El libro {libro.título} no está disponible.")

    def devolver_libro(self, libro, bibliotecario):
        if libro in self.libros_prestados:
            bibliotecario.gestionar_libro(libro, 'devolver')
            self.libros_prestados.remove(libro)
            print(f"{self.nombre} ha devuelto el libro: {libro.título}")
        else:
            print(f"{self.nombre} no tiene el libro: {libro.título}")

# Ejemplo de uso
libro1 = Libro("Cántame al Dormir", "Gilraen Earfalas", "1234567890")
bibliotecario = Bibliotecario("Cristian")
usuario = Usuario("Gabriela")

usuario.pedir_prestado(libro1, bibliotecario)
usuario.devolver_libro(libro1, bibliotecario)