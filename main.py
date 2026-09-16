#menu
def menu_principal():
    while True:
        print("\n==================== AGROCONTROL CBA ====================")
        print("1. Gestión de productos")
        print("2. Gestión de lotes productivos")
        print("3. Movimientos de inventario")
        print("4. Registrar venta")
        print("5. Consultar ventas")
        print("6. Alertas de stock")
        print("7. Reportes")
        print("8. Guardar datos")
        print("0. Salir")
        op = input("Seleccione una opción: ").strip()
        if op == "0":
            print("Hasta pronto!")
            break
        else:
            print("Opción aún no implementada.")

def main():
    print("AGROCONTROL CBA")
    menu_principal()

if __name__ == "__main__":
    main()
    




#productos 



