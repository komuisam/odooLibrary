{
    'name': "library_member",
    'summary': "Gestión de miembros de biblioteca con componente OWL",
    'description': "Módulo para gestionar miembros que heredan de res.partner y muestran un contador OWL.",
    'author': "My Company",
    'website': "",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['base', "web"],

    'data': [
        'security/ir.model.access.csv',
        'views/action_library_members.xml',
        'views/library_member_views.xml',
        'views/library_loan_views.xml',
        'views/library_book_views.xml',
        'views/library_menu_views.xml',
    ],

    'assets': {
        'web.assets_backend': [
            'library_member/static/src/components/owl_counter/owl_counter.js',
            'library_member/static/src/js/owl_counter_loader.js',
        ],
        'web.assets_qweb': [
            'library_member/static/src/components/owl_counter/owl_counter.xml',
        ],
    },

    'installable': True,
    'application': True,
}