# Curso Completo de Python para Administradores de Sistemas

## 1. Fundamentos de Python para administradores de sistemas

### Sintaxis básica
- Uso de indentación para bloques de código
- Variables y tipos de datos: int, float, str, bool
- Operadores: aritméticos (+, -, *, /, //, %, **), comparación (==, !=, <, >, <=, >=), lógicos (and, or, not)

### Ejemplo básico:
```python
nombre = "Admin"
edad = 30

if edad >= 18:
    print(f"{nombre} es mayor de edad")
else:
    print(f"{nombre} es menor de edad")
```

## 2. Configuración del entorno de desarrollo (VS Code, Git, y GitHub)

### VS Code
- Instalación: Descargar de code.visualstudio.com
- Extensiones recomendadas: Python, Git Lens

### Git
- Instalación: git-scm.com/downloads
- Configuración básica:
  ```
  git config --global user.name "Tu Nombre"
  git config --global user.email "tu@email.com"
  ```

### GitHub
- Crear cuenta en github.com
- Conectar Git local con GitHub usando SSH

## 3. Estructuras de datos y control de flujo

### Estructuras de datos
- Listas: `mi_lista = [1, 2, 3]`
- Tuplas: `mi_tupla = (1, 2, 3)`
- Diccionarios: `mi_dict = {"clave": "valor"}`
- Conjuntos: `mi_set = {1, 2, 3}`

### Control de flujo
- if, elif, else
- for loops
- while loops
- try/except para manejo de errores

```python
for i in range(5):
    try:
        resultado = 10 / i
        print(f"10 / {i} = {resultado}")
    except ZeroDivisionError:
        print("No se puede dividir por cero")
```

## 4. Funciones y módulos en Python

### Funciones
```python
def saludar(nombre):
    return f"Hola, {nombre}!"

print(saludar("Admin"))
```

### Módulos
- Importar módulos: `import os`
- Importar funciones específicas: `from os import path`
- Crear módulos propios

## 5. Programación orientada a objetos en Python

```python
class Servidor:
    def __init__(self, nombre, ip):
        self.nombre = nombre
        self.ip = ip
    
    def ping(self):
        return f"Pinging {self.ip}..."

mi_servidor = Servidor("Web1", "192.168.1.100")
print(mi_servidor.ping())
```

## 6. Manejo de archivos y directorios

```python
import os

# Listar archivos
archivos = os.listdir(".")
print(archivos)

# Leer archivo
with open("config.txt", "r") as f:
    contenido = f.read()
    print(contenido)

# Escribir archivo
with open("log.txt", "w") as f:
    f.write("Log entry")
```

## 7. Interacción con el sistema operativo

```python
import subprocess

# Ejecutar comando
resultado = subprocess.run(["ls", "-l"], capture_output=True, text=True)
print(resultado.stdout)

# Variables de entorno
import os
print(os.environ.get("PATH"))
```

## 8. Networking con Python

```python
import socket

# Crear un socket TCP/IP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conectar el socket al puerto donde el servidor está escuchando
server_address = ('localhost', 10000)
sock.connect(server_address)

try:
    # Enviar datos
    message = b'Este es el mensaje.'
    sock.sendall(message)

    # Recibir respuesta
    data = sock.recv(1024)
    print(f'Recibido: {data.decode()}')

finally:
    sock.close()
```

## 9. Automatización de tareas administrativas

```python
import schedule
import time

def backup():
    print("Realizando backup...")

schedule.every().day.at("01:00").do(backup)

while True:
    schedule.run_pending()
    time.sleep(1)
```

## 10. Manejo de bases de datos

```python
import sqlite3

conn = sqlite3.connect('example.db')
c = conn.cursor()

# Crear tabla
c.execute('''CREATE TABLE stocks
             (date text, trans text, symbol text, qty real, price real)''')

# Insertar datos
c.execute("INSERT INTO stocks VALUES ('2020-01-05','BUY','RHAT',100,35.14)")

# Guardar (commit) los cambios
conn.commit()

# Consultar datos
for row in c.execute('SELECT * FROM stocks ORDER BY price'):
    print(row)

conn.close()
```

## 11. Creación de scripts de administración

Ejemplo de script para monitorear espacio en disco:

```python
import shutil
import smtplib

def check_disk_usage(disk, min_percent):
    du = shutil.disk_usage(disk)
    percent_free = du.free / du.total * 100
    if percent_free < min_percent:
        return False
    return True

def send_alert(message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login("tu_email@gmail.com", "tu_contraseña")
    server.sendmail("tu_email@gmail.com", "admin@tuempresa.com", message)
    server.quit()

if not check_disk_usage("/", 20):
    send_alert("Alerta: Poco espacio en disco!")
```

## 12. Consumo de APIs

```python
import requests

response = requests.get('https://api.github.com/users/octocat')
if response.status_code == 200:
    data = response.json()
    print(f"Nombre: {data['name']}")
    print(f"Repositorios públicos: {data['public_repos']}")
else:
    print(f"Error: {response.status_code}")
```

## 13. Mejores prácticas y patrones de diseño

- Sigue PEP 8 para estilo de código
- Usa nombres descriptivos para variables y funciones
- Comenta tu código, pero no en exceso
- Utiliza manejo de excepciones
- Implementa patrones como Singleton, Factory, o Observer según sea necesario

## 14. Testing y debugging

```python
import unittest

def suma(a, b):
    return a + b

class TestSuma(unittest.TestCase):
    def test_suma_positivos(self):
        self.assertEqual(suma(3, 4), 7)
    
    def test_suma_negativos(self):
        self.assertEqual(suma(-1, -1), -2)

if __name__ == '__main__':
    unittest.main()
```

Para debugging, usa el debugger integrado de VS Code o pdb en la línea de comandos.

## 15. Distribución y empaquetado de aplicaciones Python

1. Crea un archivo `setup.py`:

```python
from setuptools import setup, find_packages

setup(
    name="MiApp",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'requests',
        'sqlalchemy',
    ],
)
```

2. Crea un entorno virtual: `python -m venv env`
3. Activa el entorno: `source env/bin/activate` (Linux/Mac) o `env\Scripts\activate` (Windows)
4. Instala tu paquete: `pip install -e .`

Para distribuir, puedes usar `python setup.py sdist bdist_wheel` y subir a PyPI con `twine upload dist/*`.

Este curso proporciona una base sólida en Python para administradores de sistemas. Practica cada concepto y adapta los ejemplos a tus necesidades específicas. Recuerda consultar la documentación oficial de Python y de las bibliotecas que uses para obtener información más detallada.
