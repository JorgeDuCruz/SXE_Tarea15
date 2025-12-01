# -*- coding: utf-8 -*-
{
    'name': "cafe_al_falla",

    'summary': "Módulo para ver que alumno esta mas dormido",

    'description': """
Un grupo de alumnos del Daniel Castelao, se están acostando tarde porque
estudian mucho y pican mucho código en casa. En ocasiones, a la manana
siguiente en el centro, tienen sueno en clase, pero no tienen claro por qué opción
decantarse de entre las maravillosas ofertas de los establecimientos que rodean el
centro. Como tienen dudas de qué escoger, un companero decide realizar un
módulo sencillo que establece la bebida que deben tomar en función del nivel de
sueno que tengan.    """,

    'author': "Jorge Durán Cruz",
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

