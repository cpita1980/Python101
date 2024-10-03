import platform
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
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

def guardar_informacion(info, nombre_archivo):
    """Guarda la información del sistema en un archivo."""
    with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
        archivo.write("=" * 50 + "\n")
        archivo.write("           INFORMACIÓN DEL SISTEMA\n")
        archivo.write("=" * 50 + "\n")
        for clave, valor in info.items():
            archivo.write(f"{clave:<20}: {valor}\n")
        archivo.write("=" * 50 + "\n")

class AplicacionInfoSistema:
    def __init__(self, master):
        self.master = master
        master.title("Información del Sistema")
        master.geometry("400x300")

        self.info = obtener_informacion_sistema()

        self.crear_widgets()

    def crear_widgets(self):
        # Frame principal
        main_frame = ttk.Frame(self.master, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Crear y colocar etiquetas para cada pieza de información
        for i, (clave, valor) in enumerate(self.info.items()):
            ttk.Label(main_frame, text=f"{clave}:").grid(column=0, row=i, sticky=tk.W, padx=5, pady=2)
            ttk.Label(main_frame, text=valor).grid(column=1, row=i, sticky=tk.W, padx=5, pady=2)

        # Botón para guardar la información
        ttk.Button(main_frame, text="Guardar Información", command=self.guardar_info).grid(column=0, row=len(self.info), columnspan=2, pady=10)

    def guardar_info(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Archivo de texto", "*.txt")])
        if file_path:
            guardar_informacion(self.info, file_path)
            messagebox.showinfo("Guardado", f"La información ha sido guardada en {file_path}")

def main():
    root = tk.Tk()
    app = AplicacionInfoSistema(root)
    root.mainloop()

if __name__ == "__main__":
    main()