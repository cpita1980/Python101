# Cheatsheet: Módulos Python para Administración de Sistemas

## 1. os
```python
import os

# Ejecutar comando del sistema
os.system('ls -l')

# Obtener variables de entorno
home = os.environ.get('HOME')

# Manipular rutas
ruta = os.path.join('/home', 'usuario', 'documentos')
```

## 2. subprocess
```python
import subprocess

# Ejecutar comando y capturar salida
resultado = subprocess.run(['ls', '-l'], capture_output=True, text=True)
print(resultado.stdout)

# Ejecutar comando con pipe
ps = subprocess.Popen(['ps', 'aux'], stdout=subprocess.PIPE)
output = subprocess.check_output(['grep', 'python'], stdin=ps.stdout)
```

## 3. sys
```python
import sys

# Argumentos de línea de comandos
args = sys.argv

# Salir del script
sys.exit(1)

# Información sobre la plataforma
print(sys.platform)
```

## 4. psutil
```python
import psutil

# Uso de CPU
print(psutil.cpu_percent())

# Uso de memoria
print(psutil.virtual_memory())

# Procesos en ejecución
for proc in psutil.process_iter(['pid', 'name']):
    print(proc.info)
```

## 5. paramiko (SSH)
```python
import paramiko

# Conectar a servidor SSH
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect('hostname', username='user', password='pass')

# Ejecutar comando remoto
stdin, stdout, stderr = client.exec_command('ls -l')
print(stdout.read().decode())

client.close()
```

## 6. logging
```python
import logging

logging.basicConfig(filename='app.log', level=logging.INFO)

logging.info('Iniciando aplicación')
logging.error('Ha ocurrido un error')
```

## 7. schedule
```python
import schedule
import time

def job():
    print("Ejecutando tarea programada")

schedule.every(10).minutes.do(job)
schedule.every().hour.do(job)
schedule.every().day.at("10:30").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
```

## 8. configparser
```python
import configparser

config = configparser.ConfigParser()
config['DEFAULT'] = {'ServerAliveInterval': '45',
                     'Compression': 'yes',
                     'CompressionLevel': '9'}
with open('config.ini', 'w') as configfile:
    config.write(configfile)
```

## 9. argparse
```python
import argparse

parser = argparse.ArgumentParser(description='Descripción del script')
parser.add_argument('--input', help='Archivo de entrada')
parser.add_argument('--output', help='Archivo de salida')
args = parser.parse_args()

print(args.input, args.output)
```

## 10. shutil
```python
import shutil

# Copiar archivo
shutil.copy2('origen.txt', 'destino.txt')

# Mover archivo
shutil.move('origen.txt', 'nuevo_destino.txt')

# Eliminar directorio y contenido
shutil.rmtree('directorio')
```
