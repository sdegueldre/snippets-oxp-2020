from odoo import http
from odoo.http import request

class CustomSnippets(http.Controller):
    @http.route(['/custom_snippets/cart_content'], type='json', auth="public", website=True)
    def cart(self):
        products = request.website.sale_get_order().order_line.product_id
        data = []
        for product in products:
            fields = product.read(['display_name', 'description_sale', 'list_price', 'website_url'])[0];
            fields['image'] = request.env['website'].image_url(product, 'image_512')
            data.append(fields)
        return request.env['ir.ui.view']._render_template('custom_snippets.s_cart_products_card', {'products': data})
