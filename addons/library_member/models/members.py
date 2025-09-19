# -*- coding: utf-8 -*-
from odoo import models, fields, api

class LibraryMember(models.Model):
    _inherit = 'res.partner'

    is_library_member = fields.Boolean(string="Es Miembro de Biblioteca", default=False)

    loaned_books_count = fields.Integer(
        string="Libros Prestados",
        compute="_compute_loaned_books_count",
        store=False,
    )

    loan_ids = fields.One2many(
        'library.loan',
        'member_id',  
        string="Préstamos"
    )

    @api.depends('loan_ids')
    def _compute_loaned_books_count(self):
        for member in self:
            member.loaned_books_count = len(member.loan_ids)

#####################################################
