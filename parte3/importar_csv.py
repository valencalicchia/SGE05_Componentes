import csv
import random
import datetime
import os
import sys
# Ruta absoluta al directorio raíz del proyecto
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# Añade esa ruta al sys.path
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from parte2.cuatro.table_generator import GestionTabla
from parte1.validador_contrasena import validar_contrasena
from parte1.validador_usuario import validar_nombre_usuario

class ClienteManager:
    def __init__(self, archivo_csv):
        self.archivo_csv = archivo_csv
        self.gestion = GestionTabla()
        self.gestion.cargar_csv()  # Carga datos existentes
        self.datos_existentes = {d["Nombre"]: d for d in self.gestion.datos}
        self.nuevos = 0
        self.modificados = 0

    def procesar_csv(self):
        with open(self.archivo_csv, newline='', encoding='utf-8') as csvfile:
            lector = csv.DictReader(csvfile)
            for fila in lector:
                nombre_completo = fila["Nombre del cliente"]
                nombre_parts = nombre_completo.strip().split()

                if len(nombre_parts) < 3:
                    print(f"Nombre incompleto para login: {nombre_completo}")
                    continue

                nombre, apellido1, apellido2 = nombre_parts[0], nombre_parts[1], nombre_parts[2]
                login = (nombre[0] + apellido1).lower()

                if not validar_nombre_usuario(login):
                    print(f"Login inválido: {login}")
                    continue

                password = self.generar_password(nombre, apellido1, apellido2)
                if not validar_contrasena(password):
                    print(f"Contraseña inválida generada para {nombre_completo}")
                    continue

                cliente_info = {
                    "Nombre": nombre_completo,
                    "Apellido": apellido1,
                    "Fecha Nacimiento": "",  # No viene en el CSV, campo simulado
                    "Dirección": fila["Dirección"],
                    "Contraseña": password,
                    "Teléfono": fila["Teléfono"],
                    "Email": fila["e-mail"],
                    "Web": fila["Página web"],
                    "Población": fila["Población"],
                    "Código Postal": fila["Código Postal"],
                    "Tipo": fila["Tipo"],
                    "Login": login
                }

                if nombre_completo in self.datos_existentes:
                    # Modifica datos existentes
                    self.gestion.datos = [
                        cliente_info if d["Nombre"] == nombre_completo else d
                        for d in self.gestion.datos
                    ]
                    self.modificados += 1
                else:
                    self.gestion.datos.append(cliente_info)
                    self.nuevos += 1

        self.gestion.guardar_csv()
        self.informe()

    def generar_password(self, nombre, ap1, ap2):
        partes = [nombre, ap1, ap2]
        random.shuffle(partes)
        hora = datetime.datetime.now()
        segundos = hora.second
        minutos = hora.minute
        simbolo = random.choice(['$', '%', '&'])

        passw = (
            partes[0][0] +
            str(segundos).zfill(2) +
            partes[1][1].lower() +
            partes[1][2].upper() +
            str(minutos).zfill(2) +
            (partes[2][3] if len(partes[2]) > 3 else 'x') +
            simbolo
        )
        return passw

    def informe(self):
        print("== Resultado del procesamiento ==")
        print(f"Registros añadidos: {self.nuevos}")
        print(f"Registros modificados: {self.modificados}")

if __name__ == "__main__":
    ruta_csv = input("Introduce la ruta del archivo CSV con clientes: ")
    if not os.path.isfile(ruta_csv):
        print("El archivo especificado no existe.")
    else:
        manager = ClienteManager(ruta_csv)
        manager.procesar_csv()
