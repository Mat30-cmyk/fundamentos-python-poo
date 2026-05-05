# =========================
# MÉTODOS BÁSICOS
# =========================
class Coche:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.encendido = False

    def encender(self):
        if not self.encendido:
            self.encendido = True
            return "Encendido"
        return "Ya estaba encendido"

    def apagar(self):
        if self.encendido:
            self.encendido = False
            return "Apagado"
        return "Ya estaba apagado"


c = Coche("Toyota", "Corolla")
print(c.encender())
print(c.apagar())


# =========================
# MÉTODOS CON PARÁMETROS
# =========================
class Carro:
    def __init__(self):
        self.velocidad = 0

    def acelerar(self, valor):
        self.velocidad += valor
        return self.velocidad

    def frenar(self, valor):
        self.velocidad -= valor
        if self.velocidad < 0:
            self.velocidad = 0
        return self.velocidad


carro = Carro()
print(carro.acelerar(50))
print(carro.frenar(20))


# =========================
# MÉTODOS QUE MODIFICAN ATRIBUTOS
# =========================
class Cuenta:
    def __init__(self, saldo=0):
        self._saldo = saldo

    def depositar(self, monto):
        self._saldo += monto
        return self._saldo

    def retirar(self, monto):
        if monto > self._saldo:
            return "Sin saldo"
        self._saldo -= monto
        return self._saldo


cuenta = Cuenta(100)
print(cuenta.depositar(50))
print(cuenta.retirar(30))


# =========================
# MÉTODOS QUE DEVUELVEN DATOS
# =========================
class Calculadora:
    def sumar(self, a, b):
        return a + b

    def dividir(self, a, b):
        if b == 0:
            return "Error"
        return a / b


calc = Calculadora()
print(calc.sumar(2, 3))
print(calc.dividir(10, 2))


# =========================
# MÉTODOS QUE LLAMAN A OTROS
# =========================
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def es_mayor(self):
        return self.edad >= 18

    def presentarse(self):
        if self.es_mayor():
            return f"{self.nombre} es mayor"
        return f"{self.nombre} es menor"


p = Persona("Juan", 20)
print(p.presentarse())


# =========================
# MÉTODOS ESPECIALES
# =========================
class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __add__(self, otro):
        return Punto(self.x + otro.x, self.y + otro.y)

    def __eq__(self, otro):
        return self.x == otro.x and self.y == otro.y


p1 = Punto(2, 3)
p2 = Punto(1, 1)
print(p1)
print(p1 + p2)
print(p1 == p2)


# =========================
# MÉTODOS ESTÁTICOS
# =========================
class Util:
    @staticmethod
    def es_par(n):
        return n % 2 == 0


print(Util.es_par(4))


# =========================
# MÉTODOS DE CLASE
# =========================
class Empleado:
    contador = 0

    def __init__(self, nombre):
        self.nombre = nombre
        Empleado.contador += 1

    @classmethod
    def total(cls):
        return cls.contador


e1 = Empleado("Ana")
e2 = Empleado("Luis")
print(Empleado.total())


# =========================
# EJEMPLO COMPLETO
# =========================
class Libro:
    def __init__(self, titulo):
        self.titulo = titulo
        self.abierto = False

    def abrir(self):
        self.abierto = True

    def cerrar(self):
        self.abierto = False

    def estado(self):
        return "Abierto" if self.abierto else "Cerrado"


libro = Libro("Python")
libro.abrir()
print(libro.estado())