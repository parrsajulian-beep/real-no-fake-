#menu
def menu_principal():
    print("===================================================")
    print("                 menu principal                    ")
    print("===================================================")
    print("1. gestion de productos")

















#productos 

def buscar_producto(codigo):
    codigo = codigo.upper()
    for p in productos:
        if p["codigo"] == codigo:
            return p
    return None


def listar_productos():
    if not productos:
        print("  No hay productos.")
        return
    print("\n  Código   | Nombre                  | Precio   | Stock | Estado")
    print("             |                         |          |       |       ")
    for p in productos:
        stock = calcular_stock(p["codigo"])
        estado = "Activo" if p.get("activo", True) else "Inactivo"
        print(f"  {p['codigo']:<8} | {p['nombre'][:22]:<22} | {p['precio']:>7} | {stock:>5} | {estado}")


def registrar_producto():
    print("\n--- REGISTRAR PRODUCTO ---")
    codigo = input("Código (ej: P001): ").strip().upper()
    if buscar_producto(codigo):
        print("Ese código ya existe.")
        return

    nombre = input("Nombre: ").strip()
    categoria = input("Categoría: ").strip()
    unidad = input("Unidad: ").strip()

    try:
        precio = float(input("Precio: ").strip())
        if precio <= 0:
            print("El precio debe ser mayor a 0.")
            return
    except:
        print("Precio inválido.")
        return

    try:
        stock_minimo = int(input("Stock mínimo: ").strip())
        if stock_minimo < 0:
            print("Stock mínimo no puede ser negativo.")
            return
    except:
        print("Stock mínimo inválido.")
        return

    productos.append({
        "codigo": codigo,
        "nombre": nombre,
        "categoria": categoria,
        "unidad": unidad,
        "precio": precio,
        "stock_minimo": stock_minimo,
        "activo": True
    })
    guardar_todo()
    print(f"  Producto {codigo} registrado.")


def actualizar_producto():
    print("\n--- ACTUALIZAR PRODUCTO ---")
    codigo = input("Código: ").strip().upper()
    p = buscar_producto(codigo)
    if not p:
        print("No existe ese producto.")
        return

    print(f"  Actual: {p['nombre']} | Precio: {p['precio']}")
    print("  (Deja en blanco para no cambiar)")

    nombre = input("Nuevo nombre: ").strip()
    if nombre:
        p["nombre"] = nombre

    precio = input("Nuevo precio: ").strip()
    if precio:
        try:
            p["precio"] = float(precio)
        except:
            print("Precio no válido, se mantiene el anterior.")

    guardar_todo()
    print("  Producto actualizado.")


def desactivar_producto():
    print("\n--- DESACTIVAR PRODUCTO ---")
    codigo = input("Código: ").strip().upper()
    p = buscar_producto(codigo)
    if not p:
        print("No existe ese producto.")
        return
    p["activo"] = False
    guardar_todo()
    print(f"Producto {codigo} desactivado.")


def menu_productos():
    while True:
        print("\n===== GESTIÓN DE PRODUCTOS =====")
        print("1. Registrar producto")
        print("2. Listar productos")
        print("3. Actualizar producto")
        print("4. Desactivar producto")
        print("0. Volver")
        op = input("Opción: ").strip()

        if op == "1":
            registrar_producto()
        elif op == "2":
            listar_productos()
        elif op == "3":
            actualizar_producto()
        elif op == "4":
            desactivar_producto()
        elif op == "0":
            break
        else:
            print("Opción no válida.")
