{
    'name': 'School',
    'author': 'NHCL @ Abdo',
    'summary': 'school system ',
    'category': 'Business',
    'license': 'LGPL-3',
    'version': '1.0',
    'depends': [
        'mail',
        'board',
    ],
    'data': [
        'security/ir.model.access.csv',

        'data/student_seq.xml',


        'views/dashboard.xml',
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
    'assests': {
        'web.assets_backend': [
            # 'static/src/components/school_dashboard.js'
            # 'static/src/components/school_dashboard.xml'
            # 'static/src/components/**/*.scss'

        ],
    },
}
