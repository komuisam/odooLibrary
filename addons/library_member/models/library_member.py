from odoo import models, fields, api

class LibraryMember(models.Model):
    _name = 'library.member'
    _description = 'Library Member'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _inherits = {'res.partner': 'partner_id'}

    partner_id = fields.Many2one(
        'res.partner',
        string='Related Partner',
        required=True,
        ondelete='cascade'
    )
    membership_number = fields.Char(
        string='Membership Number',
        required=True,
        default='New'
    )
    join_date = fields.Date(
        string='Join Date',
        default=fields.Date.today()
    )
    loan_count = fields.Integer(
        string='Books Loaned',
        compute='_compute_loan_count',
        store=False
    )

    @api.model
    def create(self, vals):
        if vals.get('membership_number', 'New') == 'New':
            vals['membership_number'] = self.env['ir.sequence'].next_by_code('library.member.sequence') or 'New'
        return super().create(vals)

    def _compute_loan_count(self):
        # Simulamos el conteo de libros por ahora
        for member in self:
            member.loan_count = 5

    # Asegurar que el nombre se herede del partner
    def name_get(self):
        result = []
        for member in self:
            result.append((member.id, member.partner_id.name))
        return result