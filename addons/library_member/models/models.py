# -*- coding: utf-8 -*-

from odoo import models, fields, api


class library_member(models.Model):
    _name = 'library_member.library_member'
    _description = 'library_member.library_member'

    title = fields.Char()
    count = fields.Integer()
    value = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()
    @api.depends('count')
    def _value_pc(self):
        for record in self:
            record.value = float(record.count) / 100

