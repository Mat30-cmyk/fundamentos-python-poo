# Ejemplos de Clase – Programación Orientada a Objetos en Python

En esta sección se replican los ejemplos básicos vistos en clase sobre POO en Python y Encapsulación incluyendo:

+ Clase Y Constructor
+ Atributos
+ Métodos
+ Encapsulación

Cada archivo contiene unos ejemplos simples y funcionales de la documentación, son ejecutables desde consola.

## 📁 Estructura 

```python
ejemplos_clase/
├── clase_y_constructor.py
├── metodos.py
├── atributos.py
└── encapsulacion.py
```

## Ejecutar

Desde la terminal, ubícate en la carpeta del proyecto y ejecuta:

### Clase Y Constructor
```python
python ejemplos_clase/clase_y_constructor.py
```

### Atributos
```python
python ejemplos_clase/atributos.py
```

### Métodos
```python
python ejemplos_clase/metodos.py
```

### Encapsulación
```python
python ejemplos_clase/encapsulacion.py
```

# Evidencias de Funcionamiento

## Clase y Constructor

<details>
<summary>Ver capturas de Clase y Constructor</summary>

---

## El método constructor: __init__

Mostrar:

- Creación de `ana`
- Creación de `juan`
- Impresión de atributos

![Clase Constructor 1](../capturas/Captura%20de%20pantalla%202026-05-07%20161727.png)

---

## PARÁMETRO SELF


## Valores predeterminados en el constructor

Mostrar:

- Producto con stock por defecto
- Producto con stock personalizado

![Clase Constructor 2](../capturas/Captura%20de%20pantalla%202026-05-07%20162446.png)

---

## Inicialización de atributos con cálculos

Mostrar:

- Resultado del área
- Resultado del perímetro

![Clase Constructor 3](../capturas/Captura%20de%20pantalla%202026-05-07%20162641.png)

---

## Atributos con validación

Mostrar:

- Cuenta válida
- Error ValueError

![Clase Constructor 4](../capturas/Captura%20de%20pantalla%202026-05-07%20162829.png)

---

## Ejemplo práctico: Modelando una biblioteca

Mostrar:

- Estado disponible
- Estado prestado

![Clase Constructor 5](../capturas/Captura%20de%20pantalla%202026-05-07%20163222.png)

---

## Constructores alternativos con métodos de clase

Mostrar:

- Fecha normal
- Fecha desde texto
- Fecha actual

![Clase Constructor 6](../capturas/Captura%20de%20pantalla%202026-05-07%20163357.png)

---

</details>

---

## Atributos

<details>
<summary>Ver capturas de atributos</summary>

---

# Atributos de Instancia

Mostrar:

- Creación de `e1`
- Creación de `e2`
- Impresión de nombres

![Atributos Instancia](../capturas/Captura%20de%20pantalla%202026-05-07%20164022.png)

# Atributos de clase

Mostrar:

- Valor inicial de nombre_uni
- Cambio de atributo de clase
- Nuevo valor reflejado en ambos objetos

![Atributos de clase](../capturas/Captura%20de%20pantalla%202026-05-07%20164447.png)

# Acceso de Atributos

Mostrar:

- Color inicial
- Cambio de color
- Nuevo color

![Acceso de Atributos](../capturas/Captura%20de%20pantalla%202026-05-07%20165124.png)

# Modificación de Atributos

Mostrar:

- Color inicial
- Cambio de color
- Nuevo color

![Modificación de Atributos](../capturas/Captura%20de%20pantalla%202026-05-07%20165351.png)

# Atributos Dinámicos

Mostrar:

- Atributos agregados dinámicamente
- Impresión completa

![Atributos Dinámicos](../capturas/Captura%20de%20pantalla%202026-05-07%20175850.png)

# Atributos Privados

Mostrar:

- Mostrar titular
- Mostrar _saldo
- Mostrar PIN mediante método

![Atributos Privados](../capturas/Captura%20de%20pantalla%202026-05-07%20180608.png)

# Propiedades (Getter y Setter)

Mostrar:

- Asignación válida
- Impresión de temperatura

![Propiedades (Getter y Setter)](../capturas/Captura%20de%20pantalla%202026-05-07%20180755.png)

# Atributos Calculados

Mostrar:

- Resultado del área

![Atributos Calculados](../capturas/Captura%20de%20pantalla%202026-05-07%20181001.png)

# Funciones con Atributos

Mostrar:

- Resultado de hasattr
- Resultado de getattr
- Uso de setattr
- Uso de delattr

![Funciones con Atributos](../capturas/Captura%20de%20pantalla%202026-05-07%20181112.png)

</details>

---

## Métodos

<details> 
<summary>Ver capturas de métodos</summary>

# Métodos Básicos

Mostrar:

- Encender coche
- Apagar coche

![Metodos Basicos](../capturas/metodos_basicos.png)

# Métodos con Parámetros

Mostrar:

- Acelerar
- Frenar

![Metodos Parametros](../capturas/metodos_parametros.png)

# Métodos que Modifican Atributos

Mostrar:

- Depositar dinero
- Retirar dinero

![Modificar Atributos Metodo](../capturas/metodos_modifican.png)

# Métodos que Devuelven Datos

Mostrar:

- Resultado suma
- Resultado división

![Metodos Retorno](../capturas/metodos_retorno.png)

# Métodos que Llaman Otros Métodos

Mostrar:

- Resultado de presentarse()

![Metodos Internos](../capturas/metodos_internos.png)

# Métodos Especiales

Mostrar:

- Impresión de objeto
- Suma de objetos
- Comparación de objetos

![Metodos Especiales](../capturas/metodos_especiales.png)

# Métodos Estáticos

Mostrar:

- Resultado de es_par

![Metodos Estaticos](../capturas/metodos_estaticos.png)

# Métodos de Clase

Mostrar:

- Contador de empleados

![Metodos Clase](../capturas/metodos_clase.png)

# Ejemplo Completo

Mostrar:

- Abrir libro
- Mostrar estado

![Ejemplo Completo](../capturas/ejemplo_completo.png)

</details>

---

## Encapsulación

<details>
<summary>Ver capturas de encapsulación</summary>

---

# Atributos Privados

Mostrar:

- Creación de `CuentaBancaria`
- Validación correcta del PIN
- Uso de atributos protegidos `_titular` y `_saldo`

![Atributos Privados](../capturas/encapsulacion_privados.png)

# Getters y Setters

Mostrar:

- Creación de objeto Persona
- Cambio de edad usando set_edad()
- Resultado usando get_edad()

![Getters Setters](../capturas/getters_setters.png)

# Propiedades (@property)

Mostrar:

- Conversión de Celsius a Fahrenheit
- Uso de @property
- Resultado correcto en consola

![Propiedades](../capturas/propiedades_encapsulacion.png)

# Métodos Privados

Mostrar:

- Creación del Autenticador
- Login correcto
- Funcionamiento del método privado __generar_hash

![Metodos Privados](../capturas/metodos_privados.png)

# Ejemplo Completo

Mostrar:

- Aplicación de descuento
- Precio actualizado
- Resultado final mostrado en consola

![Ejemplo Completo Encapsulacion](../capturas/ejemplo_completo_encapsulacion.png)

# Ejecución Completa del Programa

Mostrar:

- Validación de PIN
- Edad actualizada
- Temperatura en Fahrenheit
- Login exitoso
- Precio con descuento

![Salida Completa](../capturas/salida_completa_encapsulacion.png)

<details>