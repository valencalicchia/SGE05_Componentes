# stock_info/models/stock_info.py
from odoo import models, fields, api

class ProductProduct(models.Model):
    _inherit = 'product.product'

    def export_csv(self):
        """Redirige al controlador para generar el CSV."""
        return {
            'type': 'ir.actions.act_url',
            'url': '/stock/export_csv',
            'target': 'self',
        }