# Cheatsheet: Fundamentos de Python

## Tipos de datos básicos
- `int`: Enteros (1, 2, 3)
- `float`: Decimales (1.0, 2.5)
- `str`: Cadenas de texto ("Hola")
- `bool`: Booleanos (True, False)

## Variables
```python
x = 5
nombre = "Admin"
```

## Operadores
- Aritméticos: `+`, `-`, `*`, `/`, `//`, `%`, `**`
- Comparación: `==`, `!=`, `<`, `>`, `<=`, `>=`
- Lógicos: `and`, `or`, `not`

## Estructuras de control
```python
# If-elif-else
if condicion:
    # código
elif otra_condicion:
    # código
else:
    # código

# For loop
for item in iterable:
    # código

# While loop
while condicion:
    # código

# Try-except
try:
    # código que puede causar error
except TipoDeError:
    # manejo del error
```

## Funciones
```python
def nombre_funcion(parametro1, parametro2):
    # código
    return resultado
```

## Listas, Tuplas, Diccionarios
```python
mi_lista = [1, 2, 3]
mi_tupla = (1, 2, 3)
mi_dict = {"clave": "valor"}
```

## Métodos de cadenas útiles
- `str.upper()`, `str.lower()`: Mayúsculas/minúsculas
- `str.strip()`: Elimina espacios en blanco
- `str.split()`: Divide la cadena en una lista
