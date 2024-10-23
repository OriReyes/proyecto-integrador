productos = []

while True:
    print("\n--- Menú de Gestión de Inventario ---")
    print("1. Agregar producto")
    print("2. Mostrar productos")
    print("3. Borrar producto")
    print("4. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        nombre = input("Ingrese el nombre del producto: ").strip().lower()
        precio = float(input("Ingrese el precio del producto: "))
        cantidad = int(input("Ingrese la cantidad del producto: "))

        producto_existente = False
        i = 0
        while i < len(productos):
            if productos[i][0] == nombre:
                print("El producto ya existe. Actualizando la cantidad...")
                productos[i][2] += cantidad
                print(f"Ahora hay {productos[i][2]} unidades de {nombre}.")
                producto_existente = True
                break
            i += 1

        if not producto_existente:
            productos.append([nombre, precio, cantidad])
            print("Producto agregado exitosamente.")

    elif opcion == "2":
        if not productos:
            print("No hay productos en el inventario.")
        else:
            i = 0
            while i < len(productos):
                print(f"Nombre: {productos[i][0]}, Precio: {productos[i][1]}, Cantidad: {productos[i][2]}")
                i += 1

    elif opcion == "3":
        nombre = input("Ingrese el nombre del producto que desea borrar: ").strip().lower()
        i = 0
        while i < len(productos):
            if productos[i][0] == nombre:
                productos.pop(i)
                print(f"Producto {nombre} borrado exitosamente.")
                break
            i += 1
        else:
            print(f"Producto {nombre} no encontrado en el inventario.")

    elif opcion == "4":
        print("Saliendo del programa...")
        break

    else:
        print("Opción inválida. Por favor, intente nuevamente.")
