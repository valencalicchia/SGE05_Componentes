# -*- coding: utf-8 -*-


from odoo import models, fields, api, _
class ResPartner(models.Model):
    _inherit = 'res.partner'

    login = fields.Char(string="Login")
    x_password = fields.Char(string="Contraseña")