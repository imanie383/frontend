# -*- coding: utf-8 -*-
{
    'name': "Academy B&F",
    'category': 'Website',
    'description': "Generic modulo for Bend And Frank",
    'version': '11.0',
    # instala el modulo de website, marca error en el modulo graph
    'depends': ['website'],
    # actulizar lista de aplicaciones desde la app. modeo debug
    # always loaded Importa el orden
    'data': [
        'views/template.xml',
        'views/attributes.xml',
        'views/teacher.xml'
    ],
    'demo': [
        'data/demo.xml',
    ],
    'instalable': True,
    'auto_install': True,
}
