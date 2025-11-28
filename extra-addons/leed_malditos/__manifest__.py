# -*- coding: utf-8 -*-
{
    'name': "leed_malditos",

    'summary': "Módulo para contar las veces que un profesor manda leer a los alumnos",

    'description': """
Si esta es la descripción.
    """,

    'author': "Daniel Castelao",
    'website': "https://www.google.com/url?sa=t&source=web&rct=j&opi=89978449&url=https://www.youtube.com/watch%3Fv%3DdQw4w9WgXcQ&ved=2ahUKEwjKh7KD-5SRAxUJ1wIHHRrAEP4QwqsBegQIEhAB&usg=AOvVaw0aHtehaphMhOCAkCydRLZU",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

