# stock_info/controllers/main.py
from odoo import http
from odoo.http import request
import csv
from io import StringIO

class StockInfoController(http.Controller):

    @http.route('/stock/export_csv', type='http', auth='user')
    def export_stock_csv(self):
        """Genera un archivo CSV con el stock de todos los productos."""
        # Obtener todos los productos ordenados por descripción
        productos = request.env['product.product'].search([], order='name asc')

        # Crear un archivo CSV en memoria
        output = StringIO()
        writer = csv.writer(output)
        writer.writerow(['Código', 'Descripción', 'Stock Actual'])

        # Escribir los datos de cada producto
        for producto in productos:
            writer.writerow([producto.default_code, producto.name, producto.qty_available])

        # Preparar la respuesta para descargar el archivo
        output.seek(0)
        response = request.make_response(
            output.getvalue(),
            headers=[
                ('Content-Type', 'text/csv'),
                ('Content-Disposition', 'attachment; filename=stock_productos.csv')
            ]
        )
        return response