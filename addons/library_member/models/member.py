# library_member/models/member.py
from odoo import models, fields, api

class LibraryMember(models.Model):
    _name = 'library.member'
    _inherits = {'res.partner': 'partner_id'}
    _description = 'Library Member'

    partner_id = fields.Many2one(
        'res.partner',
        ondelete='cascade',
        required=True,
        string='Partner'
    )
    loan_count = fields.Integer(
        string='Books Loaned',
        compute='_compute_loan_count'
    )

    @api.depends()
    def _compute_loan_count(self):
        # Suponiendo que existe un modelo `library.loan` que tiene un campo `member_id`
        Loan = self.env['library.loan']
        for member in self:
            count = Loan.search_count([('member_id', '=', member.id)])
            member.loan_count = count