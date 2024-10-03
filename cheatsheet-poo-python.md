# Cheatsheet: Programación Orientada a Objetos en Python

## Definición de clase
```python
class MiClase:
    def __init__(self, atributo):
        self.atributo = atributo
    
    def metodo(self):
        return f"Valor del atributo: {self.atributo}"
```

## Creación de objetos
```python
mi_objeto = MiClase("valor")
```

## Herencia
```python
class ClaseHija(ClasePadre):
    def __init__(self, atributo, nuevo_atributo):
        super().__init__(atributo)
        self.nuevo_atributo = nuevo_atributo
```

## Métodos especiales
- `__str__`: Representación en string
- `__len__`: Longitud del objeto
- `__eq__`: Comparación de igualdad

## Propiedades
```python
class MiClase:
    @property
    def mi_propiedad(self):
        return self._mi_propiedad

    @mi_propiedad.setter
    def mi_propiedad(self, valor):
        self._mi_propiedad = valor
```

## Métodos estáticos y de clase
```python
class MiClase:
    @staticmethod
    def metodo_estatico():
        # No necesita self

    @classmethod
    def metodo_de_clase(cls):
        # Recibe la clase como primer argumento
```
