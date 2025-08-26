# models/loan.py
from odoo import models, fields

class LibraryLoan(models.Model):
    _name = 'library.loan'
    _description = 'Book Loan'

    member_id = fields.Many2one('library.member', string='Member', required=True)
    book_title = fields.Char(string='Book Title')