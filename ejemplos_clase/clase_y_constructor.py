# =========================================
# CLASE Y CONSTRUCTOR - TODOS LOS EJEMPLOS
# =========================================


# -----------------------------------------
# 1. CLASE BÁSICA
# -----------------------------------------
class Persona:
    pass


# -----------------------------------------
# 2. CONSTRUCTOR (__init__)
# -----------------------------------------
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad


# Crear objetos
ana = Persona("Ana García", 28)
juan = Persona("Juan López", 35)

print(ana.nombre)   # Ana García
print(juan.edad)    # 35


# -----------------------------------------
# 3. PARÁMETRO SELF
# -----------------------------------------

# Python internamente hace algo parecido a:
# Persona.__init__(ana, "Ana García", 28)

print("\n--- SELF ---")
print(ana.nombre)
print(ana.edad)


# -----------------------------------------
# 4. VALORES PREDETERMINADOS
# -----------------------------------------
class Producto:
    def __init__(self, nombre, precio, stock=0):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock


laptop = Producto("Laptop XPS", 1200)
teclado = Producto("Teclado Mecánico", 80, 15)

print("\n--- PRODUCTOS ---")
print(laptop.stock)     # 0
print(teclado.stock)    # 15


# -----------------------------------------
# 5. INICIALIZACIÓN CON CÁLCULOS
# -----------------------------------------
class Rectangulo:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto
        self.area = ancho * alto
        self.perimetro = 2 * (ancho + alto)


rect = Rectangulo(5, 3)

print("\n--- RECTÁNGULO ---")
print(rect.area)        # 15
print(rect.perimetro)   # 16


# -----------------------------------------
# 6. VALIDACIÓN EN EL CONSTRUCTOR
# -----------------------------------------
class Cuenta:
    def __init__(self, titular, saldo_inicial):
        self.titular = titular

        if saldo_inicial < 0:
            raise ValueError("El saldo inicial no puede ser negativo")

        self.saldo = saldo_inicial


print("\n--- CUENTAS ---")

# Cuenta válida
cuenta_ana = Cuenta("Ana García", 1000)
print(cuenta_ana.saldo)

# Cuenta inválida
try:
    cuenta_error = Cuenta("Juan López", -500)
except ValueError as e:
    print("Error:", e)


# -----------------------------------------
# 7. EJEMPLO PRÁCTICO: LIBRO
# -----------------------------------------
class Libro:
    def __init__(self, titulo, autor, paginas, isbn, disponible=True):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.isbn = isbn
        self.disponible = disponible
        self.pagina_actual = 0


libro1 = Libro(
    "Python Crash Course",
    "Eric Matthes",
    544,
    "9781593279288"
)

libro2 = Libro(
    "Clean Code",
    "Robert C. Martin",
    464,
    "9780132350884",
    False
)

print("\n--- LIBROS ---")
print(f"{libro1.titulo} está {'disponible' if libro1.disponible else 'prestado'}")
print(f"{libro2.titulo} está {'disponible' if libro2.disponible else 'prestado'}")


# -----------------------------------------
# 8. CONSTRUCTORES ALTERNATIVOS
# -----------------------------------------
class Fecha:
    def __init__(self, dia, mes, año):
        self.dia = dia
        self.mes = mes
        self.año = año

    @classmethod
    def desde_texto(cls, texto):
        dia, mes, año = map(int, texto.split('-'))
        return cls(dia, mes, año)

    @classmethod
    def hoy(cls):
        import datetime

        fecha_actual = datetime.date.today()

        return cls(
            fecha_actual.day,
            fecha_actual.month,
            fecha_actual.year
        )


fecha1 = Fecha(15, 3, 2023)
fecha2 = Fecha.desde_texto("25-12-2023")
fecha3 = Fecha.hoy()

print("\n--- FECHAS ---")
print(f"{fecha1.dia}/{fecha1.mes}/{fecha1.año}")
print(f"{fecha2.dia}/{fecha2.mes}/{fecha2.año}")
print(f"{fecha3.dia}/{fecha3.mes}/{fecha3.año}")


# =========================================
# FIN
# =========================================

print("\n🔥 Todos los ejemplos ejecutados correctamente")