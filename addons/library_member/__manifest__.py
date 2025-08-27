{
    'name': 'Library Members',
    'version': '17.0.1.0.0',
    'category': 'Library',
    'summary': 'Manage library members',
    'description': """
        Manage library members and track book loans.
    """,
    'author': 'Tu Nombre',
    'website': 'https://www.tuwebsite.com',
    'depends': ['base', 'contacts'],
    'data': [
        'security/ir.model.access.csv',  # PRIMERO seguridad
        'models/library_member.py',      # LUEGO modelos
        'views/library_member_views.xml', # FINALMENTE vistas
    ],
    'assets': {
        'web.assets_backend': [
            'library_member/static/src/js/member_loan_count.js',
            'library_member/static/src/js/loan_count_widget.xml',
            'library_member/static/src/css/style.css',
        ],
    },
    'installable': True,
    'application': True,
    'auto_install': False,
}