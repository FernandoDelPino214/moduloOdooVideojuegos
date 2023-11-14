# -*- coding: utf-8 -*-
{
    'name': "videojuegos",
    'summary': """gestion de una tienda de venta de videojuegos""",
    'description': """
        Modulo para gestionar la venta de videojuegos
    """,
    'author': "Fernando del Pino",
    'website': "noTengoPaginaWeb.net",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'prueba',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'views.xml',
    ],
}
