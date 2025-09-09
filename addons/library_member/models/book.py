# -*- coding: utf-8 -*-

from odoo import models, fields, api

class LibraryBook(models.Model):
    _name = 'library.book'
    _description = 'Libro de Biblioteca'
    
    name = fields.Char(string="Título", required=True)
    author = fields.Char(string="Autor")
    isbn = fields.Char(string="ISBN")
    active = fields.Boolean(string="Activo", default=True)