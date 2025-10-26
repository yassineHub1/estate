# Create a odoo manifest
{
    'name': 'estate.property',
    'version': '1.0',
    'author': 'Yassine',
    'category': 'Real Estate',
    'summary': 'A module to manage real estate operations including property listings, client management, and sales tracking.',
    'description': """
        Estate Management System
        ========================
        This module helps in managing real estate operations
    """,
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/estate_property_view.xml',
        'views/estate_property_menu_view.xml'
    ],
    'demo': [],
    'auto_install': True,
    'license': 'LGPL-3',
}