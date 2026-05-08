# =========================
# ATRIBUTOS DE INSTANCIA
# =========================
class Estudiante:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.activo = True

e1 = Estudiante("Ana", 20)
e2 = Estudiante("Luis", 22)

print(e1.nombre)
print(e2.nombre)


# =========================
# ATRIBUTOS DE CLASE
# =========================
class Universidad:
    nombre_uni = "Universidad X"

    def __init__(self, estudiante):
        self.estudiante = estudiante

u1 = Universidad("Ana")
u2 = Universidad("Luis")

print(u1.nombre_uni)
print(u2.nombre_uni)

Universidad.nombre_uni = "Nueva Universidad"

print(u1.nombre_uni)
print(u2.nombre_uni)


# =========================
# ACCESO DE ATRIBUTOS
# =========================
class Producto:
    impuesto = 0.21  # Atributo de clase

    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

# Creamos un producto
laptop = Producto("Laptop", 1000)

# Accedemos a sus atributos
print(laptop.nombre)    # Atributo de instancia
print(laptop.precio)    # Atributo de instancia
print(laptop.impuesto)  # Atributo de clase (accedido desde la instancia)
print(Producto.impuesto)  # Atributo de clase (accedido desde la clase)


class Coche:
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.kilometraje = 0

# =========================
# MODIFICACIÓN DE ATRIBUTOS
# =========================

# Creamos un coche nuevo
mi_coche = Coche("Toyota", "Corolla", "Azul")
print(f"Color inicial: {mi_coche.color}")  # Imprime: Color inicial: Azul
print(f"Kilometraje inicial: {mi_coche.kilometraje}")  # Imprime: Kilometraje inicial: 0

# Modificamos sus atributos
mi_coche.color = "Rojo"  # Pintamos el coche
mi_coche.kilometraje = 1500  # Actualizamos el kilometraje

print(f"Nuevo color: {mi_coche.color}")  # Imprime: Nuevo color: Rojo
print(f"Kilometraje actual: {mi_coche.kilometraje}")  # Imprime: Kilometraje actual: 1500

# =========================
# ATRIBUTOS DINÁMICOS
# =========================
class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

# Creamos una persona
juan = Persona("Juan")

# Añadimos atributos dinámicamente
juan.edad = 30
juan.profesion = "Ingeniero"

print(f"{juan.nombre} tiene {juan.edad} años y es {juan.profesion}")
# Imprime: Juan tiene 30 años y es Ingeniero



# =========================
# ATRIBUTOS PRIVADOS
# =========================
class Cuenta:
    def __init__(self, titular, saldo, pin):
        self.titular = titular
        self._saldo = saldo
        self.__pin = pin

    def mostrar_pin(self):
        return self.__pin

cuenta = Cuenta("Ana", 1000, "1234")

print(cuenta.titular)
print(cuenta._saldo)  # se puede, pero no deberías
print(cuenta.mostrar_pin())


# =========================
# PROPIEDADES (GET/SET)
# =========================
class Temperatura:
    def __init__(self):
        self._celsius = 0

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, valor):
        if valor < -273:
            print("Error")
        else:
            self._celsius = valor

t = Temperatura()
t.celsius = 25
print(t.celsius)


# =========================
# ATRIBUTOS CALCULADOS
# =========================
class Rectangulo:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    @property
    def area(self):
        return self.ancho * self.alto

r = Rectangulo(5, 3)
print(r.area)


# =========================
# FUNCIONES CON ATRIBUTOS
# =========================
class Ejemplo:
    def __init__(self, valor):
        self.valor = valor

obj = Ejemplo(10)

print(hasattr(obj, "valor"))
print(getattr(obj, "valor"))

setattr(obj, "nuevo", 50)
print(obj.nuevo)

delattr(obj, "nuevo")