import csv
import base64
import logging
from odoo import models, fields, api

_logger = logging.getLogger(__name__)

class ImportClientes(models.Model):
    _name = "import.clientes"
    _description = "Importación de Clientes desde CSV"

    archivo_csv = fields.Binary("Archivo CSV", required=True)

    def importar_clientes(self):
        """Lee el archivo CSV y crea clientes en Odoo."""
        self.ensure_one()
        if not self.archivo_csv:
            raise ValueError("¡Debe subir un archivo CSV!")

        # Decodificar el archivo
        datos = base64.b64decode(self.archivo_csv).decode("utf-8").splitlines()
        lector = csv.DictReader(datos)

        cliente_modelo = self.env["res.partner"]

        for fila in lector:
            tipo = fila["Tipo"]
            is_customer = tipo in ["C", "T"]
            is_supplier = tipo in ["P", "T"]

            cliente_data = {
                "name": fila["Nombre a mostrar"],
                "street": fila["Dirección"],
                "phone": fila["Teléfono"],
                "email": fila["e-mail"],
                "website": fila["Página web"],
                "city": fila["Población"],
                "zip": fila["Código Postal"],
                "customer_rank": 1 if is_customer else 0,
                "supplier_rank": 1 if is_supplier else 0,
            }

            cliente = cliente_modelo.create(cliente_data)
            _logger.info(f"Cliente {cliente.name} agregado con ID {cliente.id}")

        return {
            "type": "ir.actions.client",
            "tag": "reload",
        }
