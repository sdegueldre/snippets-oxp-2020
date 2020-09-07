{
    'name': 'Custom Snippets',
    'category': 'Website/Website',
    'sequence': 51,
    'summary': 'Adds custom snippets website',
    'version': '1.0',
    'description': "",
    'depends': ['website_sale'],
    'qweb': ['static/src/xml/*.xml'],
    'data': [
        'views/snippets/snippets.xml',
        'views/snippets/s_cart_products.xml',
    ],
    'installable': True,
    'application': True,
}
