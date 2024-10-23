class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

class Inventario:
    def __init__(self):
        self.productos = []

    def agregar_producto(self):
        nombre = input("Ingrese el nombre del producto: ").strip().lower()  # Normaliza el nombre
        precio = float(input("Ingrese el precio del producto: "))
        cantidad = int(input("Ingrese la cantidad del producto: "))
        
        for producto in self.productos:
            if producto.nombre == nombre:
                print("El producto ya existe. Actualizando la cantidad...")
                producto.cantidad += cantidad
                print(f"Ahora hay {producto.cantidad} unidades de {producto.nombre}.")
                return
        
        nuevo_producto = Producto(nombre, precio, cantidad)
        self.productos.append(nuevo_producto)
        print("Producto agregado exitosamente.")

    def mostrar_productos(self):
        if not self.productos:
            print("No hay productos en el inventario.")
        else:
            productos_str = "\n".join([f"Nombre: {producto.nombre}, Precio: {producto.precio}, Cantidad: {producto.cantidad}" for producto in self.productos])
            print("Productos en el inventario:\n" + productos_str)

    def borrar_producto(self):
        nombre = input("Ingrese el nombre del producto que desea borrar: ").strip().lower()  # Normaliza el nombre
        for producto in self.productos:
            if producto.nombre == nombre:
                self.productos.remove(producto)
                print(f"Producto {nombre} borrado exitosamente.")
                return
        print(f"Producto {nombre} no encontrado en el inventario.")

def mostrar_menu():
    inventario = Inventario()
    while True:
        print("\n--- Menú de Gestión de Inventario ---")
        print("1. Agregar producto")
        print("2. Mostrar productos")
        print("3. Borrar producto")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            inventario.agregar_producto()
        elif opcion == "2":
            inventario.mostrar_productos()
        elif opcion == "3":
            inventario.borrar_producto()
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Por favor, intente nuevamente.")

# Ejemplo de ejecución del menú
mostrar_menu()
