# -*- coding: utf-8 -*-


from odoo import models, fields, api

class LibraryMember(models.Model):
    _inherit = 'res.partner'  # Extiende el modelo de contactos de Odoo

    title = fields.Many2one('res.partner.title')
    count = fields.Integer()
    value = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()
    
    # Campo para contar libros prestados
    loaned_books_count = fields.Integer(
        string="Libros Prestados",
        compute="_compute_loaned_books_count",
        store=False,  # No se almacena porque se calcula en tiempo real
        help="Número total de libros prestados a este miembro"
    )
    
    # Relación con préstamos (asumiendo que existe un modelo library.loan)
    # Si no existe, necesitarás crearlo primero
    loan_ids = fields.One2many(
        'library.loan',  # Nombre del modelo de préstamos
        'member_id',     # Campo en library.loan que referencia al miembro
        string="Préstamos"
    )

    @api.depends('count')
    def _value_pc(self):
        for record in self:
            record.value = float(record.count) / 100

    @api.depends('loan_ids')
    def _compute_loaned_books_count(self):
        for member in self:
            member.loaned_books_count = len(member.loan_ids)