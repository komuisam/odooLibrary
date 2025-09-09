# -*- coding: utf-8 -*-

from odoo import models, fields, api

class LibraryMember(models.Model):
    _inherit = 'res.partner'  # Extiende el modelo de contactos de Odoo

    title = fields.Many2one('res.partner.title')
    count = fields.Integer()
    value = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()

    @api.depends('count')
    def _value_pc(self):
        for record in self:
            record.value = float(record.count) / 100
