{
    'name': 'Custom Snippets',
    'category': 'Website/Website',
    'sequence': 51,
    'summary': 'Adds custom snippets website',
    'version': '1.0',
    'description': "",
    'depends': ['website', 'website_sale', 'web'],
    'qweb': ['static/src/xml/*.xml'],
    'data': [
        'views/snippets/snippets.xml',
        'views/snippets/s_cart_products.xml',
    ],

    # assets
    'assets':{
        "web.assets_frontend":[
            "/custom_snippets/static/src/snippets/s_cart_products/000.js",
        ],

        "web.assets_editor":[
            "/custom_snippets/static/src/snippets/s_cart_products/options.js",
        ],
    },

    'installable': True,
    'application': True,
}
