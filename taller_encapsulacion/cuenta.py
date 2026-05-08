# =========================
# TALLER ENCAPSULACIÓN
# =========================

class CuentaBancaria:
    def __init__(self, titular, saldo=0):
        self._titular = titular
        self._saldo = saldo

    # -------------------------
    # PROPIEDAD SOLO LECTURA
    # -------------------------
    @property
    def titular(self):
        return self._titular

    # -------------------------
    # PROPIEDAD CON VALIDACIÓN
    # -------------------------
    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        if valor < 0:
            raise ValueError("El saldo no puede ser negativo")
        self._saldo = valor

    # -------------------------
    # MÉTODOS
    # -------------------------
    def depositar(self, cantidad):
        if cantidad > 0:
            self._saldo += cantidad
            return True
        return False

    def retirar(self, cantidad):
        if cantidad > 0 and cantidad <= self._saldo:
            self._saldo -= cantidad
            return True
        return False


# =========================
# PRUEBAS
# =========================
# =========================
# SISTEMA INTERACTIVO
# =========================

cuenta = CuentaBancaria("Teo", 1000)

while True:
    print("\n--- MENÚ ---")
    print("1. Ver saldo")
    print("2. Depositar")
    print("3. Retirar")
    print("4. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        print(f"💰 Saldo actual: {cuenta.saldo}")

    elif opcion == "2":
        try:
            monto = float(input("¿Cuánto quieres depositar? "))
            if cuenta.depositar(monto):
                print("✅ Depósito exitoso")
            else:
                print("❌ Monto inválido")
        except:
            print("❌ Eso no es un número bro")

    elif opcion == "3":
        try:
            monto = float(input("¿Cuánto quieres retirar? "))
            if cuenta.retirar(monto):
                print("✅ Retiro exitoso")
            else:
                print("❌ Fondos insuficientes o monto inválido")
        except:
            print("❌ Eso no es un número ")

    elif opcion == "4":
        print("👋 Chao, gracias")
        break

    else:
        print("❌ Opción inválida, aprende a leer 😒")