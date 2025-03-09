import json


class Libro:
    def __init__(self, isbn, titulo, autor, categoria, prestado=False):
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.prestado = prestado

    def to_dict(self):
        return {
            "isbn": self.isbn,
            "titulo": self.titulo,
            "autor": self.autor,
            "categoria": self.categoria,
            "prestado": self.prestado
        }


class Usuario:
    def __init__(self, id_usuario, nombre):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.libros_prestados = []

    def prestar_libro(self, libro):
        """Añade un libro a la lista de libros prestados."""
        self.libros_prestados.append(libro)

    def devolver_libro(self, libro):
        """Elimina un libro de la lista de libros prestados."""
        if libro in self.libros_prestados:
            self.libros_prestados.remove(libro)

    def listar_libros_prestados(self):
        """Devuelve la lista de libros actualmente prestados al usuario."""
        return [libro.titulo for libro in self.libros_prestados]


class Biblioteca:
    def __init__(self, archivo_json='biblioteca.json'):
        self.archivo_json = archivo_json
        self.libros = self.cargar_libros()
        self.usuarios = {}

    def cargar_libros(self):
        try:
            with open(self.archivo_json, 'r') as archivo:
                datos_libros = json.load(archivo)
                return {isbn: Libro(**datos) for isbn, datos in datos_libros.items()}
        except FileNotFoundError:
            return {}

    def guardar_libros(self):
        with open(self.archivo_json, 'w') as archivo:
            json.dump({isbn: libro.to_dict() for isbn, libro in self.libros.items()}, archivo, indent=4)

    def añadir_libro(self, libro):
        if libro.isbn not in self.libros:
            self.libros[libro.isbn] = libro
            self.guardar_libros()
            print(f"Libro '{libro.titulo}' añadido con éxito.")
        else:
            print("Error: El libro ya existe en la biblioteca.")

    def registrar_usuario(self, id_usuario, nombre):
        if id_usuario not in self.usuarios:
            usuario = Usuario(id_usuario, nombre)
            self.usuarios[id_usuario] = usuario
            print(f"Usuario '{nombre}' registrado con éxito.")
        else:
            print("Error: El usuario ya está registrado.")

    def prestar_libro(self, isbn, id_usuario):
        libro = self.libros.get(isbn)
        usuario = self.usuarios.get(id_usuario)

        if libro and not libro.prestado and usuario:
            libro.prestado = True
            usuario.prestar_libro(libro)
            self.guardar_libros()
            print(f"Libro '{libro.titulo}' prestado a {usuario.nombre}.")
        else:
            print("Error en el préstamo del libro.")

    def devolver_libro(self, isbn, id_usuario):
        libro = self.libros.get(isbn)
        usuario = self.usuarios.get(id_usuario)

        if libro and libro.prestado and usuario:
            libro.prestado = False
            usuario.devolver_libro(libro)
            self.guardar_libros()
            print(f"Libro '{libro.titulo}' devuelto por {usuario.nombre}.")
        else:
            print("Error en la devolución del libro.")

    def mostrar_libros(self):
        for libro in self.libros.values():
            estado = "Prestado" if libro.prestado else "Disponible"
            print(f"{libro.isbn}: {libro.titulo} por {libro.autor} - {estado}")

    def buscar_libro(self, criterio):
        resultados = [libro for libro in self.libros.values()
                      if criterio.lower() in libro.titulo.lower() or
                      criterio.lower() in libro.autor.lower() or
                      criterio.lower() in libro.categoria.lower()]

        if resultados:
            for libro in resultados:
                estado = "Prestado" if libro.prestado else "Disponible"
                print(f"{libro.isbn}: {libro.titulo} por {libro.autor} - {estado}")
        else:
            print("No se encontraron libros que coincidan con el criterio.")


def menu():
    biblioteca = Biblioteca()

    while True:
        print(
            "\n1. Añadir Libro\n2. Mostrar Libros\n3. Prestar Libro\n4. Devolver Libro\n5. Registrar Usuario\n6. Buscar Libro\n7. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            isbn = input("ISBN: ")
            titulo = input("Título: ")
            autor = input("Autor: ")
            categoria = input("Categoría: ")
            libro = Libro(isbn, titulo, autor, categoria)
            biblioteca.añadir_libro(libro)

        elif opcion == '2':
            biblioteca.mostrar_libros()

        elif opcion == '3':
            isbn = input("ISBN del libro a prestar: ")
            id_usuario = input("ID del usuario que lo solicita: ")
            biblioteca.prestar_libro(isbn, id_usuario)

        elif opcion == '4':
            isbn = input("ISBN del libro a devolver: ")
            id_usuario = input("ID del usuario que lo devuelve: ")
            biblioteca.devolver_libro(isbn, id_usuario)

        elif opcion == '5':
            id_usuario = input("ID del nuevo usuario: ")
            nombre = input("Nombre del nuevo usuario: ")
            biblioteca.registrar_usuario(id_usuario, nombre)

        elif opcion == '6':
            criterio = input("Ingrese título, autor o categoría para buscar: ")
            biblioteca.buscar_libro(criterio)

        elif opcion == '7':
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    menu()
