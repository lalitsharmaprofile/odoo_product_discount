from odoo.addons.website_sale.controllers.main import WebsiteSale
from odoo import http
from odoo.http import request

class WebsiteSaleInherit(WebsiteSale):

    def _website_product_price(self, product):
        """
        Override to include the discounted price in the shop page.
        """
        res = super()._website_product_price(product)
        if product.discount_percentage > 0:
            res.update({
                'price': product.discounted_price,
                'has_discount': True,
                'original_price': product.list_price
            })
        return res
