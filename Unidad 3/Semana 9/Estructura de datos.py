class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"{self.nombre}, Cantidad: {self.cantidad}, Precio: ${self.precio}"

class Inventario:
    def __init__(self):
        # Usamos un diccionario para almacenar los productos, con el ID como clave
        self.productos = {}

    def agregar_producto(self, producto):
        if producto.id_producto in self.productos:
            print("Error: Producto ya existe.")
        else:
            self.productos[producto.id_producto] = producto
            print("Producto agregado correctamente.")

    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
            print("Producto eliminado correctamente.")
        else:
            print("Error: Producto no encontrado.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        if id_producto in self.productos:
            if cantidad is not None:
                self.productos[id_producto].cantidad = cantidad
            if precio is not None:
                self.productos[id_producto].precio = precio
            print("Producto actualizado correctamente.")
        else:
            print("Error: Producto no encontrado.")

    def buscar_producto(self, nombre):
        encontrados = []
        for producto in self.productos.values():
            if nombre.lower() in producto.nombre.lower():
                encontrados.append(producto)
        if encontrados:
            for producto in encontrados:
                print(producto)
        else:
            print("No se encontraron productos con ese nombre.")

    def mostrar_inventario(self):
        if self.productos:
            for producto in self.productos.values():
                print(producto)
        else:
            print("El inventario está vacío.")

# Interfaz de usuario en la consola
def menu():
    inventario = Inventario()
    while True:
        print("\n1. Agregar Producto\n2. Eliminar Producto\n3. Actualizar Producto\n4. Buscar Producto\n5. Mostrar Inventario\n6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '6':
            print("Saliendo del programa...")
            break

        elif opcion == '1':
            try:
                id_producto = input("Ingrese el ID del producto: ")
                nombre = input("Ingrese el nombre del producto: ")
                cantidad = int(input("Ingrese la cantidad: "))
                precio = float(input("Ingrese el precio: "))
                nuevo_producto = Producto(id_producto, nombre, cantidad, precio)
                inventario.agregar_producto(nuevo_producto)
            except ValueError:
                print("Error: Ingrese valores válidos para la cantidad y el precio.")
            except Exception as e:
                print(f"Error inesperado: {e}") # Captura otros errores

        elif opcion == '2':
            try:
                id_eliminar = input("Ingrese el ID del producto a eliminar: ")
                inventario.eliminar_producto(id_eliminar)
            except Exception as e:
                print(f"Error inesperado: {e}")

        elif opcion == '3':
            try:
                id_actualizar = input("Ingrese el ID del producto a actualizar: ")
                cantidad_str = input("Ingrese la nueva cantidad (deje vacío si no cambia): ")
                precio_str = input("Ingrese el nuevo precio (deje vacío si no cambia): ")

                cantidad = int(cantidad_str) if cantidad_str else None
                precio = float(precio_str) if precio_str else None

                inventario.actualizar_producto(id_actualizar, cantidad, precio)
            except ValueError:
                print("Error: Ingrese valores válidos para la cantidad y el precio.")
            except Exception as e:
                print(f"Error inesperado: {e}")

        elif opcion == '4':
            nombre_buscar = input("Ingrese el nombre del producto a buscar: ")
            inventario.buscar_producto(nombre_buscar)

        elif opcion == '5':
            inventario.mostrar_inventario()

        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu()
