from odoo import fields, models, api


class ProductCategoryLine(models.Model):
    _name = "product.category.line"
    _description = "Product Category Table Line"

    picking_id = fields.Many2one("stock.picking", string="Picking")
    category = fields.Many2one("product.category", string="Product Category")
    demand = fields.Float(string="Demand")
    done = fields.Float(string="Done")
