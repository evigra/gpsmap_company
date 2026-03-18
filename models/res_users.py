import datetime
import requests
import random
from dateutil.relativedelta import relativedelta
from odoo import http, api, fields, models, _
from odoo.http import request


class res_users(models.Model):
    _inherit = "res.users"

    customer_ids = fields.Many2many(
        'res.partner',
        'res_partner_related_rel',  # tabla relacional
        'partner_id',               # columna origen
        'related_partner_id',       # columna destino
        string='Contactos Relacionados'
    )

    
    def write(self, vals):
        res = super().write(vals)

        # Si cambió la relación de partners, limpiar cachés de seguridad
        if 'customer_ids' in vals:
            self.env['ir.rule'].clear_caches()
            self.env['ir.model.access'].clear_caches()

        return res    
