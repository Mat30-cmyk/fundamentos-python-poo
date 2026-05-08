# ==========================================
# SISTEMA DE PRÉSTAMOS DE EQUIPOS
# ==========================================

from datetime import datetime

# ==========================================
# DICCIONARIO PRINCIPAL
# ==========================================
equipos = {
    "Laptop Dell": {
        "disponible": True,
        "prestamos": []
    },
    "Monitor Samsung": {
        "disponible": True,
        "prestamos": []
    },
    "Teclado Logitech": {
        "disponible": True,
        "prestamos": []
    }
}


# ==========================================
# MOSTRAR EQUIPOS
# ==========================================
def mostrar_equipos():
    print("\n========== EQUIPOS ==========")

    for nombre, datos in equipos.items():
        estado = "Disponible ✅" if datos["disponible"] else "Prestado ❌"
        print(f"- {nombre} → {estado}")

    print("=============================\n")


# ==========================================
# REGISTRAR PRÉSTAMO
# ==========================================
def registrar_prestamo():
    mostrar_equipos()

    equipo = input("Ingrese el nombre del equipo: ")

    if equipo not in equipos:
        print("❌ El equipo no existe.")
        return

    if not equipos[equipo]["disponible"]:
        print("⚠️ El equipo ya está prestado.")
        return

    usuario = input("Ingrese el nombre del usuario: ")

    fecha = datetime.now().strftime("%d/%m/%Y %H:%M")

    prestamo = (usuario, fecha)

    equipos[equipo]["prestamos"].append(prestamo)
    equipos[equipo]["disponible"] = False

    print(f"✅ Préstamo registrado correctamente para '{equipo}'.")


# ==========================================
# DEVOLVER EQUIPO
# ==========================================
def devolver_equipo():
    equipo = input("Ingrese el nombre del equipo a devolver: ")

    if equipo not in equipos:
        print("❌ El equipo no existe.")
        return

    if equipos[equipo]["disponible"]:
        print("⚠️ El equipo ya estaba disponible.")
        return

    equipos[equipo]["disponible"] = True

    print(f"✅ Equipo '{equipo}' devuelto correctamente.")


# ==========================================
# VER HISTORIAL
# ==========================================
def ver_historial():
    print("\n========== HISTORIAL ==========")

    for nombre, datos in equipos.items():
        print(f"\n📌 {nombre}")

        if len(datos["prestamos"]) == 0:
            print("Sin préstamos registrados.")
        else:
            for usuario, fecha in datos["prestamos"]:
                print(f"- Usuario: {usuario} | Fecha: {fecha}")

    print("\n===============================\n")


# ==========================================
# AGREGAR EQUIPO
# ==========================================
def agregar_equipo():
    nombre = input("Ingrese el nombre del nuevo equipo: ")

    if nombre in equipos:
        print("⚠️ Ese equipo ya existe.")
        return

    equipos[nombre] = {
        "disponible": True,
        "prestamos": []
    }

    print(f"✅ Equipo '{nombre}' agregado correctamente.")


# ==========================================
# MENÚ PRINCIPAL
# ==========================================
def menu():
    while True:
        print("""
=================================
 SISTEMA DE PRÉSTAMOS 💻
=================================
1. Ver equipos
2. Registrar préstamo
3. Devolver equipo
4. Ver historial
5. Agregar equipo
6. Salir
=================================
""")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mostrar_equipos()

        elif opcion == "2":
            registrar_prestamo()

        elif opcion == "3":
            devolver_equipo()

        elif opcion == "4":
            ver_historial()

        elif opcion == "5":
            agregar_equipo()

        elif opcion == "6":
            print("👋 Saliendo del sistema...")
            break

        else:
            print("❌ Opción inválida.")


# ==========================================
# EJECUCIÓN
# ==========================================
menu()