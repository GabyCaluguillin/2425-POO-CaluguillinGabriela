import pickle

# Clase Producto
class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_cantidad(self):
        return self.cantidad

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def get_precio(self):
        return self.precio

    def set_precio(self, precio):
        self.precio = precio

    def __str__(self): #Para imprimir el producto de forma legible
        return f"ID: {self.id}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}"

# Clase Inventario
class Inventario:
    def __init__(self):
        # Usamos un diccionario para almacenar los productos, donde la clave es el ID.
        self.productos = {}

    def agregar_producto(self, producto):
        if producto.get_id() not in self.productos:
            self.productos[producto.get_id()] = producto
            print(f"Producto {producto.get_nombre()} agregado al inventario.")
        else:
            print(f"Error: El producto con ID {producto.get_id()} ya existe.")

    def eliminar_producto(self, id):
        if id in self.productos:
            del self.productos[id]
            print(f"Producto con ID {id} eliminado del inventario.")
        else:
            print(f"Error: No se encontró ningún producto con ID {id}.")

    def actualizar_cantidad(self, id, cantidad):
        if id in self.productos:
            self.productos[id].set_cantidad(cantidad)
            print(f"Cantidad del producto con ID {id} actualizada a {cantidad}.")
        else:
            print(f"Error: No se encontró ningún producto con ID {id}.")

    def actualizar_precio(self, id, precio):
        if id in self.productos:
            self.productos[id].set_precio(precio)
            print(f"Precio del producto con ID {id} actualizado a {precio}.")
        else:
            print(f"Error: No se encontró ningún producto con ID {id}.")

    def buscar_producto_por_nombre(self, nombre):
        resultados = []
        for id, producto in self.productos.items():
            if nombre.lower() in producto.get_nombre().lower(): #busqueda sin importar mayusculas
                resultados.append(producto)
        return resultados

    def mostrar_inventario(self):
        if self.productos:
            print("\nInventario:")
            for id, producto in self.productos.items():
                print(producto) # Usamos el __str__ de la clase Producto
        else:
            print("El inventario está vacío.")

# Funciones para guardar y cargar el inventario
def guardar_inventario(inventario, nombre_archivo="inventario.pkl"):
    try:
        with open(nombre_archivo, 'wb') as archivo: #wb = escritura binaria
            pickle.dump(inventario.productos, archivo)
        print(f"Inventario guardado en {nombre_archivo}")
    except Exception as e:
        print(f"Error al guardar el inventario: {e}")

def cargar_inventario(nombre_archivo="inventario.pkl"):
    inventario = Inventario()
    try:
        with open(nombre_archivo, 'rb') as archivo: #rb = lectura binaria
            inventario.productos = pickle.load(archivo)
        print(f"Inventario cargado desde {nombre_archivo}")
    except FileNotFoundError:
        print("Archivo de inventario no encontrado. Se iniciará un nuevo inventario.")
    except Exception as e:
        print(f"Error al cargar el inventario: {e}")
    return inventario

# Menú principal
def mostrar_menu():
    print("\n--- Menú de Inventario ---")
    print("1. Agregar Producto")
    print("2. Eliminar Producto")
    print("3. Actualizar Cantidad")
    print("4. Actualizar Precio")
    print("5. Buscar Producto por Nombre")
    print("6. Mostrar Inventario")
    print("7. Guardar Inventario")
    print("8. Cargar Inventario")
    print("0. Salir")

def ejecutar_opcion(inventario, opcion):
    if opcion == "1":
        id = input("Ingrese el ID del producto: ")
        nombre = input("Ingrese el nombre del producto: ")
        cantidad = int(input("Ingrese la cantidad del producto: "))
        precio = float(input("Ingrese el precio del producto: "))
        producto = Producto(id, nombre, cantidad, precio)
        inventario.agregar_producto(producto)
    elif opcion == "2":
        id = input("Ingrese el ID del producto a eliminar: ")
        inventario.eliminar_producto(id)
    elif opcion == "3":
        id = input("Ingrese el ID del producto para actualizar cantidad: ")
        cantidad = int(input("Ingrese la nueva cantidad: "))
        inventario.actualizar_cantidad(id, cantidad)
    elif opcion == "4":
        id = input("Ingrese el ID del producto para actualizar precio: ")
        precio = float(input("Ingrese el nuevo precio: "))
        inventario.actualizar_precio(id, precio)
    elif opcion == "5":
        nombre = input("Ingrese el nombre del producto a buscar: ")
        resultados = inventario.buscar_producto_por_nombre(nombre)
        if resultados:
            print("\nResultados de búsqueda:")
            for producto in resultados:
                print(producto)
        else:
            print("No se encontraron productos con ese nombre.")
    elif opcion == "6":
        inventario.mostrar_inventario()
    elif opcion == "7":
        guardar_inventario(inventario)
    elif opcion == "8":
        inventario = cargar_inventario()
        return inventario #Actualiza el inventario cargado
    elif opcion == "0":
        print("Saliendo del programa...")
        return None #Indica que el bucle principal debe terminar
    else:
        print("Opción inválida. Intente de nuevo.")
    return inventario #Mantiene el inventario actual

# Programa Principal
inventario = cargar_inventario() # Cargar al inicio
while True:
    mostrar_menu()
    opcion = input("Ingrese una opción: ")
    inventario = ejecutar_opcion(inventario, opcion) #Actualiza el valor de 'inventario'
    if inventario is None:
        break #Termina el bucle si se elige salir

print("Programa finalizado.")
