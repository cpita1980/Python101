# Cheatsheet: Networking en Python

## Sockets
```python
import socket

# Crear un socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conectar a un servidor
s.connect(('hostname', port))

# Enviar datos
s.send(b'Datos a enviar')

# Recibir datos
data = s.recv(1024)

# Cerrar conexión
s.close()
```

## Requests (HTTP)
```python
import requests

# GET request
response = requests.get('https://api.example.com/data')

# POST request
response = requests.post('https://api.example.com/data', data={'key': 'value'})

# Verificar status code
if response.status_code == 200:
    data = response.json()

# Manejar autenticación
response = requests.get('https://api.example.com/protected', auth=('user', 'pass'))
```

## Parametrización de URLs
```python
from urllib.parse import urlencode, quote_plus

params = {'key1': 'value1', 'key2': 'value2'}
url = 'https://api.example.com/endpoint?' + urlencode(params, quote_via=quote_plus)
```

## Servidor HTTP simple
```python
from http.server import HTTPServer, SimpleHTTPRequestHandler

def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()

run()
```

## Trabajar con direcciones IP
```python
import ipaddress

ip = ipaddress.ip_address('192.168.1.1')
network = ipaddress.ip_network('192.168.1.0/24')

for addr in network:
    print(addr)
```
