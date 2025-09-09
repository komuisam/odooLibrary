# -*- coding: utf-8 -*-

from odoo import models, fields, api

class LibraryLoan(models.Model):
    _name = 'library.loan'
    _description = 'Préstamo de Libro'
    _order = 'loan_date desc'
    
    book_id = fields.Many2one(
        'library.book',
        string="Libro",
        required=True
    )
    member_id = fields.Many2one(
        'res.partner',
        string="Miembro",
        required=True
    )
    loan_date = fields.Date(string="Fecha de préstamo", default=fields.Date.today)
    return_date = fields.Date(string="Fecha de devolución")
    state = fields.Selection([
        ('loaned', 'Prestado'),
        ('returned', 'Devuelto'),
    ], string="Estado", default='loaned')