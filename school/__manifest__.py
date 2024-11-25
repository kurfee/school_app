{
    'name': 'School',
    'author': 'NHCL @ Abdo',
    'summary': 'school system ',
    'category': 'Business',
    'license': 'LGPL-3',
    'sequence': '-1',
    'version': '1.0',
    'depends': [
        'mail',
        'board',
    ],
    'data': [
        'security/ir.model.access.csv',

        'data/student_seq.xml',


        'views/dashboard.xml',
        'views/company_res.xml',
        'views/sale_order.xml',
        'views/students_master.xml',
        'views/subjects_master.xml',
        'views/marks_calculation.xml',
        'views/menus.xml',
    ],
    'demo': [

    ],

    'installable': True,
    'application': True,
    'auto_installable': False,
    'images': ['static/description/icon.png'
               ],
    'assets': {
        'web.assets_backend': [
            'school/static/src/components/**/*.js',
            'school/static/src/components/**/*.xml',
            'school/static/src/components/**/*.scss',
        ],
    },
}
