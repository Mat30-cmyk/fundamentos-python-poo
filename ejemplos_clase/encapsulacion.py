# =========================
# ENCAPSULACIÓN COMPLETA
# =========================

# -------------------------
# 1. ATRIBUTOS PRIVADOS
# -------------------------
class CuentaBancaria:
    def __init__(self, titular, saldo, pin):
        self._titular = titular      # protegido
        self._saldo = saldo          # protegido
        self.__pin = pin             # privado

    def validar_pin(self, pin):
        return self.__pin == pin


# -------------------------
# 2. GETTERS Y SETTERS
# -------------------------
class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad

    def get_nombre(self):
        return self._nombre

    def set_nombre(self, nombre):
        if nombre:
            self._nombre = nombre

    def get_edad(self):
        return self._edad

    def set_edad(self, edad):
        if 0 <= edad <= 120:
            self._edad = edad


# -------------------------
# 3. PROPIEDADES (@property)
# -------------------------
class Temperatura:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, valor):
        if valor < -273.15:
            raise ValueError("Muy frío 💀")
        self._celsius = valor

    @property
    def fahrenheit(self):
        return self._celsius * 9/5 + 32


# -------------------------
# 4. MÉTODOS PRIVADOS
# -------------------------
class Autenticador:
    def __init__(self, usuario, contraseña):
        self._usuario = usuario
        self._hash = self.__generar_hash(contraseña)

    def __generar_hash(self, texto):
        import hashlib
        return hashlib.sha256(texto.encode()).hexdigest()

    def login(self, contraseña):
        return self.__generar_hash(contraseña) == self._hash


# -------------------------
# 5. EJEMPLO COMPLETO
# -------------------------
class Producto:
    def __init__(self, nombre, precio):
        self._nombre = nombre
        self._precio = precio
        self._descuento = 0

    @property
    def precio(self):
        return self._precio * (1 - self._descuento)

    @precio.setter
    def precio(self, valor):
        if valor < 0:
            raise ValueError("Precio inválido 💀")
        self._precio = valor

    def aplicar_descuento(self, d):
        if 0 <= d <= 1:
            self._descuento = d


# -------------------------
# 6. USO
# -------------------------
if __name__ == "__main__":
    # Cuenta
    cuenta = CuentaBancaria("Teo", 1000, "1234")
    print(cuenta.validar_pin("1234"))

    # Persona
    p = Persona("Teo", 20)
    p.set_edad(21)
    print(p.get_edad())

    # Temperatura
    t = Temperatura(25)
    print(t.fahrenheit)

    # Autenticador
    auth = Autenticador("teo", "123")
    print(auth.login("123"))

    # Producto
    prod = Producto("Laptop", 1000)
    prod.aplicar_descuento(0.2)
    print(prod.precio)