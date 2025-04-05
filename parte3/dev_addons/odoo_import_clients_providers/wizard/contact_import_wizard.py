import base64
import csv
import io
import random
from datetime import datetime

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class ContactImportWizard(models.TransientModel):
    _name = 'contact.import.wizard'
    _description = 'Importador de Clientes/Proveedores'

    file = fields.Binary(string="Archivo CSV", required=True)
    filename = fields.Char(string="Nombre del archivo")


    def _generate_login(self, nombre_completo):
        partes = nombre_completo.lower().split()
        if len(partes) < 2:
            raise ValidationError("El nombre completo debe tener al menos nombre y apellido.")
        return partes[0][0] + partes[1]

    def _generate_password(self, nombre, apellido1, apellido2):
        elementos = [nombre, apellido1, apellido2]
        random.shuffle(elementos)

        ahora = datetime.now()
        segundos = ahora.second
        minutos = ahora.minute

        # ejemplo: M43aJ55a&
        parte1 = elementos[0][0] if elementos[0] else ''
        parte2 = str(segundos)
        parte3 = elementos[1][1:3] if len(elementos[1]) >= 3 else ''
        parte3 = parte3[0] + parte3[1].upper() if len(parte3) == 2 else ''
        parte4 = str(minutos)
        parte5 = elementos[2][3] if len(elementos[2]) >= 4 else ''
        parte6 = random.choice(['$', '%', '&'])

        password = f"{parte1}{parte2}{parte3}{parte4}{parte5}{parte6}"
        return password

    def _validate_login(self, login):
        # Aquí debes integrar la validación del módulo de Actividad 1
        # Simulación: longitud mínima de 3 caracteres
        return len(login) >= 3

    def _validate_password(self, password):
        # Aquí debes integrar la validación del módulo de Actividad 2
        # Simulación: al menos 6 caracteres y un símbolo especial
        return (
            len(password) >= 6
            and any(c in password for c in ['$', '%', '&'])
        )

    def import_contacts(self):
        if not self.file:
            raise ValidationError("Debe subir un archivo CSV válido.")

        data = base64.b64decode(self.file)
        file_stream = io.StringIO(data.decode("utf-8"))
        reader = csv.DictReader(file_stream)

        # Categorías
        categoria_cliente = self.env.ref('cliente_proveedor_import.category_customer')
        categoria_proveedor = self.env.ref('cliente_proveedor_import.category_supplier')

        añadidos = 0
        modificados = 0

        for row in reader:
            nombre = row.get("Nombre del cliente", "").strip()
            display_name = row.get("Nombre a mostrar", "").strip()
            direccion = row.get("Dirección", "").strip()
            telefono = row.get("Teléfono", "").strip()
            email = row.get("e-mail", "").strip()
            web = row.get("Página web", "").strip()
            ciudad = row.get("Población", "").strip()
            cp = row.get("Código Postal", "").strip()
            tipo = row.get("Tipo", "").strip().upper()

            if not nombre:
                continue  # saltar si no tiene nombre

            # Login y contraseña
            partes_nombre = nombre.split()
            if len(partes_nombre) < 3:
                raise ValidationError(f"Nombre incompleto: '{nombre}'. Se requiere nombre, apellido1 y apellido2.")

            nombre_simple, apellido1, apellido2 = partes_nombre[:3]
            login = self._generate_login(nombre)
            password = self._generate_password(nombre_simple, apellido1, apellido2)

            if not self._validate_login(login):
                raise ValidationError(f"Login inválido generado: {login}")

            if not self._validate_password(password):
                raise ValidationError(f"Contraseña inválida generada para {nombre}")

            contacto = self.env['res.partner'].search([('name', '=', nombre)], limit=1)

            valores = {
                'name': nombre,
                'display_name': display_name,
                'street': direccion,
                'phone': telefono,
                'email': email,
                'website': web,
                'city': ciudad,
                'zip': cp,
                'login': login,
                'x_password': password,
            }

            # Categorías
            categorias = []
            if tipo == 'C':
                categorias.append(categoria_cliente.id)
            elif tipo == 'P':
                categorias.append(categoria_proveedor.id)
            elif tipo == 'T':
                categorias += [categoria_cliente.id, categoria_proveedor.id]

            valores['category_id'] = [(6, 0, categorias)]

            if contacto:
                contacto.write(valores)
                modificados += 1
            else:
                self.env['res.partner'].create(valores)
                añadidos += 1

        mensaje = f"Importación finalizada:\n- Registros añadidos: {añadidos}\n- Registros modificados: {modificados}"
        return {
            'type': 'ir.actions.act_window',
            'name': 'Resultado de la Importación',
            'view_mode': 'form',
            'res_model': 'contact.import.wizard',
            'target': 'new',
            'context': self.env.context,
            'views': [(False, 'form')],
            'res_id': self.id,
            'warning': {'title': "Importación completada", 'message': mensaje},
        }
