{
    'name': 'Gestión de Propiedades',
    'version': '19.0.1.0.0',
    'summary': 'Módulo de práctica',
    'category': 'Real Estate',
    'author': 'Ignacio Quiero Zepeda',
    'license': 'LGPL-3',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/propiedad_views.xml',
        'views/res_partner_views.xml',
        'views/menus.xml',
    ],
    'application': True,
    'installable': True,
}
