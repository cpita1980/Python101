import platform
import socket
from datetime import datetime
from socket import gethostname, gethostbyname, gaierror

def obtener_informacion_sistema():
    """Recopila información del sistema y la devuelve en un diccionario."""
    nombre_equipo = gethostname()

    try:
        direccion_ip = gethostbyname(nombre_equipo)
    except gaierror as err:
        direccion_ip = f"No se pudo obtener la dirección IP: {err}"

    sistema_operativo = platform.system()
    version_so = platform.release()
    arquitectura = platform.machine()
    fecha_hora_actual = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    info = {
        'Fecha y hora actual': fecha_hora_actual,
        'Nombre del equipo': nombre_equipo,
        'Dirección IP': direccion_ip,
        'Sistema Operativo': f"{sistema_operativo} {version_so}",
        'Arquitectura': arquitectura
    }

    return info

def mostrar_informacion(info):
    """Muestra la información del sistema en la consola."""
    print("=" * 50)
    print("           INFORMACIÓN DEL SISTEMA")
    print("=" * 50)
    for clave, valor in info.items():
        print(f"{clave:<20}: {valor}")
    print("=" * 50)

def guardar_informacion(info, nombre_archivo):
    """Guarda la información del sistema en un archivo."""
    with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
        archivo.write("=" * 50 + "\n")
        archivo.write("           INFORMACIÓN DEL SISTEMA\n")
        archivo.write("=" * 50 + "\n")
        for clave, valor in info.items():
            archivo.write(f"{clave:<20}: {valor}\n")
        archivo.write("=" * 50 + "\n")

def main():
    info = obtener_informacion_sistema()
    mostrar_informacion(info)
    guardar_informacion(info, 'info_sistema.txt')
    print(f"\nLa información también ha sido guardada en el archivo 'info_sistema.txt'.")

if __name__ == "__main__":
    main()
