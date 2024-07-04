{
    'name': 'restrict_product_user',
    'version': '1.0',
    'summary': "Restric products for users",
    'sequence': 10,
    'author': "Anand Shah",
    'description': """
This module will helps you to only access products related to allowed categories
""",
    'depends': [ 'base', 'product','mail'],
    'data': [
        'security/security.xml',
        'views/res_users.xml'
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}
