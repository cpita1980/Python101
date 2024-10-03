# Cheatsheet: Manejo de Archivos en Python

## Abrir y cerrar archivos
```python
# Usando with (recomendado)
with open('archivo.txt', 'r') as f:
    contenido = f.read()

# Método tradicional
f = open('archivo.txt', 'r')
contenido = f.read()
f.close()
```

## Modos de apertura
- `'r'`: Lectura (por defecto)
- `'w'`: Escritura (sobrescribe)
- `'a'`: Añadir al final
- `'r+'`: Lectura y escritura

## Lectura de archivos
```python
# Leer todo el contenido
contenido = f.read()

# Leer línea por línea
for linea in f:
    print(linea)

# Leer todas las líneas en una lista
lineas = f.readlines()
```

## Escritura en archivos
```python
f.write('Texto a escribir')
f.writelines(['Línea 1\n', 'Línea 2\n'])
```

## Manejo de directorios
```python
import os

# Listar contenidos
os.listdir('ruta/del/directorio')

# Crear directorio
os.mkdir('nuevo_directorio')

# Cambiar directorio
os.chdir('ruta/del/directorio')

# Obtener directorio actual
os.getcwd()
```

## Rutas de archivos
```python
import os.path

# Unir rutas
ruta = os.path.join('directorio', 'subdirectorio', 'archivo.txt')

# Comprobar existencia
os.path.exists('archivo.txt')

# Obtener nombre de archivo y extensión
nombre, extension = os.path.splitext('archivo.txt')
```
