import json
from pathlib import Path
from datetime import datetime


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
    


BASE_DIR = Path(__file__).parent
DATA_DIR = BASE_DIR / "data"

ARCHIVOS = {
    "productos": DATA_DIR / "productos.json",
    "lotes": DATA_DIR / "lotes.json",
    "movimientos": DATA_DIR / "movimientos.json",
    "ventas": DATA_DIR / "ventas.json",
}

productos, lotes, movimientos, ventas = [], [], [], []

def asegurar_carpeta_data():
    DATA_DIR.mkdir(parents=True, exist_ok=True)

def cargar_json(ruta):
    if not ruta.exists():
        return []
    try:
        with open(ruta, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data if isinstance(data, list) else []
    except:
        return []

def guardar_json(ruta, datos):
    asegurar_carpeta_data()
    with open(ruta, "w", encoding="utf-8") as f:
        json.dump(datos, f, ensure_ascii=False, indent=2)
    return True

def cargar_todo():
    global productos, lotes, movimientos, ventas
    productos = cargar_json(ARCHIVOS["productos"])
    lotes = cargar_json(ARCHIVOS["lotes"])
    movimientos = cargar_json(ARCHIVOS["movimientos"])
    ventas = cargar_json(ARCHIVOS["ventas"])
    print("  Datos cargados.")

def guardar_todo():
    guardar_json(ARCHIVOS["productos"], productos)
    guardar_json(ARCHIVOS["lotes"], lotes)
    guardar_json(ARCHIVOS["movimientos"], movimientos)
    guardar_json(ARCHIVOS["ventas"], ventas)
    print("  Datos guardados.")



