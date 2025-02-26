from odoo import models, fields, api

class ProductTemplate(models.Model):
    _inherit = "product.template"

    discount_percentage = fields.Float(string="Discount (%)", default=0.0)
    discounted_price = fields.Float(
        string="Discounted Price",
        compute="_compute_discounted_price",
        store=True
    )

    @api.depends('list_price', 'discount_percentage')
    def _compute_discounted_price(self):
        for product in self:
            if product.discount_percentage > 0:
                product.discounted_price = product.list_price * (1 - product.discount_percentage / 100)
            else:
                product.discounted_price = product.list_price


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    @api.depends('product_id', 'product_uom_qty')
    def _compute_price_unit(self):
        for line in self:
            if line.product_id.discount_percentage > 0:
                line.price_unit = line.product_id.discounted_price
            else:
                line.price_unit = line.product_id.lst_price
