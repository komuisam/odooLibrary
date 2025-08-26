# library_member/__manifest__.py
{
    'name': 'Library Member',
    'version': '1.0',
    'summary': 'Manage library members and their book loans',
    'category': 'Services/Library',
    'depends': ['base', 'web'],
    'data': [
        'security/ir.model.access.csv',
        'views/member_views.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'library_member/static/src/components/LoanCounter.js',
            'library_member/static/src/xml/loan_counter_template.xml',
        ],
    },
    'installable': True,
    'application': True,
    'license': 'AGPL-3',
}