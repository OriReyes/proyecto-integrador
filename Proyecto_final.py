import sqlite3

# Función para conectar a la base de datos
def conectar():
    return sqlite3.connect('inventario.db')

# Función para crear la tabla de productos
def crear_tabla():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS productos (
        id INTEGER PRIMARY KEY,
        nombre TEXT NOT NULL COLLATE NOCASE,
        descripcion TEXT NOT NULL,
        cantidad INTEGER NOT NULL,
        precio REAL NOT NULL,
        categoria TEXT NOT NULL
    )
    ''')
    conn.commit()
    conn.close()

# Función para validar nombre
def validar_nombre():
    while True:
        nombre = input("Ingrese el nombre del producto: ").strip()
        if nombre:
            return nombre
        else:
            print("El nombre no puede estar vacío. Por favor, ingrese un nombre válido.")

# Función para validar descripción
def validar_descripcion():
    while True:
        descripcion = input("Ingrese la descripción del producto: ").strip()
        if descripcion:
            return descripcion
        else:
            print("La descripción no puede estar vacía. Por favor, ingrese una descripción válida.")

# Función para validar cantidad
def validar_cantidad():
    while True:
        cantidad = input("Ingrese la cantidad: ").strip()
        if cantidad.isdigit():
            return int(cantidad)
        else:
            print("Cantidad inválida. Por favor, ingrese un número entero.")

# Función para validar precio
def validar_precio():
    while True:
        precio = input("Ingrese el precio: ").strip()
        try:
            precio = float(precio)
            if precio >= 0:
                return precio
            else:
                print("El precio no puede ser negativo. Por favor, ingrese un precio válido.")
        except ValueError:
            print("Precio inválido. Por favor, ingrese un número real.")

# Función para validar categoría
def validar_categoria():
    while True:
        categoria = input("Ingrese la categoría: ").strip()
        if categoria.isalpha():  # Verifica que la categoría solo contenga letras
            return categoria
        else:
            print("La categoría solo puede contener letras. Por favor, ingrese una categoría válida.")

# Función para agregar o actualizar un producto
def agregar_actualizar_producto():
    conn = conectar()
    cursor = conn.cursor()
    
    nombre = validar_nombre()
    descripcion = validar_descripcion()
    cantidad = validar_cantidad()
    precio = validar_precio()
    categoria = validar_categoria()
    
    # Verificar si el producto ya existe
    cursor.execute('SELECT * FROM productos WHERE nombre = ?', (nombre,))
    producto = cursor.fetchone()
    
    if producto:
        # Producto existente: actualizar la cantidad y posiblemente otros detalles
        nueva_cantidad = producto[3] + cantidad
        cursor.execute('''
        UPDATE productos
        SET descripcion = ?, cantidad = ?, precio = ?, categoria = ?
        WHERE nombre = ?
        ''', (descripcion, nueva_cantidad, precio, categoria, nombre))
        print("Producto actualizado exitosamente.")
    else:
        # Producto no existente: agregar nuevo producto
        cursor.execute('''
        INSERT INTO productos (nombre, descripcion, cantidad, precio, categoria)
        VALUES (?, ?, ?, ?, ?)
        ''', (nombre, descripcion, cantidad, precio, categoria))
        print("Producto agregado exitosamente.")
    
    conn.commit()
    conn.close()

# Función para actualizar un producto
def actualizar_producto():
    conn = conectar()
    cursor = conn.cursor()
    
    while True:
        id_producto = input("Ingrese el ID del producto que desea actualizar: ").strip()
        if id_producto.isdigit():
            id_producto = int(id_producto)
            break
        else:
            print("ID inválido. Por favor, ingrese un número entero.")
    
    nombre = validar_nombre()
    descripcion = validar_descripcion()
    cantidad = validar_cantidad()
    precio = validar_precio()
    categoria = validar_categoria()
    
    cursor.execute('''
    UPDATE productos SET nombre = ?, descripcion = ?, cantidad = ?, precio = ?, categoria = ?
    WHERE id = ?
    ''', (nombre, descripcion, cantidad, precio, categoria, id_producto))
    
    conn.commit()
    conn.close()
    print("Producto actualizado exitosamente.")

# Función para eliminar un producto
def eliminar_producto():
    conn = conectar()
    cursor = conn.cursor()
    
    while True:
        id_producto = input("Ingrese el ID del producto que desea eliminar: ").strip()
        if id_producto.isdigit():
            id_producto = int(id_producto)
            break
        else:
            print("ID inválido. Por favor, ingrese un número entero.")
    
    cursor.execute('DELETE FROM productos WHERE id = ?', (id_producto,))
    
    conn.commit()
    conn.close()
    print("Producto eliminado exitosamente.")

# Función para mostrar todos los productos
def mostrar_productos():
    conn = conectar()
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM productos')
    productos = cursor.fetchall()
    
    if productos:
        for producto in productos:
            print(f"ID: {producto[0]}, Nombre: {producto[1]}, Descripción: {producto[2]}, Cantidad: {producto[3]}, Precio: {producto[4]}, Categoría: {producto[5]}")
    else:
        print("No hay productos en el inventario.")
    
    conn.close()

# Función para generar un reporte de stock bajo
def generar_reporte_stock():
    conn = conectar()
    cursor = conn.cursor()
    
    limite_stock = validar_cantidad()
    
    cursor.execute('SELECT * FROM productos WHERE cantidad < ?', (limite_stock,))
    productos_bajo_stock = cursor.fetchall()
    
    if productos_bajo_stock:
        print("\nProductos con stock bajo el límite especificado:")
        for producto in productos_bajo_stock:
            print(f"ID: {producto[0]}, Nombre: {producto[1]}, Descripción: {producto[2]}, Cantidad: {producto[3]}, Precio: {producto[4]}, Categoría: {producto[5]}")
    else:
        print("No hay productos con stock bajo el límite especificado.")
    
    conn.close()

# Función para buscar un producto por ID
def buscar_producto_por_id():
    conn = conectar()
    cursor = conn.cursor()
    
    while True:
        id_producto = input("Ingrese el ID del producto que desea buscar: ").strip()
        if id_producto.isdigit():
            id_producto = int(id_producto)
            cursor.execute('SELECT * FROM productos WHERE id = ?', (id_producto,))
            producto = cursor.fetchone()
            if producto:
                print(f"ID: {producto[0]}, Nombre: {producto[1]}, Descripción: {producto[2]}, Cantidad: {producto[3]}, Precio: {producto[4]}, Categoría: {producto[5]}")
                break
            else:
                print("Producto no encontrado. Por favor, ingrese un ID válido.")
        else:
            print("ID inválido. Por favor, ingrese un número entero.")
    
    conn.close()

# Función del menú principal
def menu():
    crear_tabla()
    
    while True:
        print("\n--- Menú de Gestión de Inventario ---")
        print("1. Agregar o actualizar producto")
        print("2. Actualizar producto")
        print("3. Eliminar producto")
        print("4. Mostrar productos")
        print("5. Generar reporte de stock")
        print("6. Buscar producto por ID")
        print("7. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_actualizar_producto()
        elif opcion == "2":
            actualizar_producto()
        elif opcion == "3":
            eliminar_producto()
        elif opcion == "4":
            mostrar_productos()
        elif opcion == "5":
            generar_reporte_stock()
        elif opcion == "6":
            buscar_producto_por_id()
        elif opcion == "7":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Por favor, intente nuevamente.")

# Ejecución del menú principal
menu()
