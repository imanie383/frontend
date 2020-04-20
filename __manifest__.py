# -*- coding: utf-8 -*-
{
    'name': "Academy B&F",
    'category': 'Website',
    'description': "Generic modulo for Bend And Frank",
    'version': '11.0',
    # any module necessary for this one to work correctly
    'depends': ['base', 'board'],
    # actulizar lista de aplicaciones desde la app. modeo debug
    # always loaded Importa el orden
    'data': [
        'views/template.xml',
        'views/attributes.xml'
    ],
    'instalable': True,
    'auto_install': True,
}
