from odoo import fields, models, api


class StockPicking(models.Model):
    _inherit = "stock.picking"

    category_ids = fields.One2many("product.category.line", "picking_id", string="Categories")
    print_in_pdf = fields.Boolean(string="Print in PDF?")

    def action_confirm(self):
        # Call the original 'Mark as Todo' button action
        res = super(StockPicking, self).action_confirm()

        # Update the category_ids after 'Mark as Todo' is clicked
        self._update_category_ids()

        return res

    def write(self, vals):
        # Use a flag to prevent recursion
        update_category_flag = vals.get('move_ids_without_package', False)
        res = super(StockPicking, self).write(vals)

        # If there's a change in the stock moves, update the category lines
        if update_category_flag:
            self._update_category_ids()

        return res

    def _update_category_ids(self):
        for rec in self:
            category_dict = {}

            # Process each stock move line
            for line in rec.move_ids_without_package:
                category_id = line.product_id.categ_id.id

                # Check if the category already exists in the temporary dictionary
                if category_id in category_dict:
                    # Update existing category quantities
                    category_dict[category_id]['demand'] += line.product_uom_qty
                    category_dict[category_id]['done'] += line.quantity
                else:
                    # Create a new category line if it doesn't exist yet
                    category_dict[category_id] = {
                        "category": category_id,
                        "demand": line.product_uom_qty,
                        "done": line.quantity,  # This ensures `done` is updated
                    }

            # Convert the dictionary into One2many lines and update the category_ids field
            category_lines = [(0, 0, data) for data in category_dict.values()]
            rec.category_ids = [(5, 0, 0)] + category_lines  # Clear existing lines and replace with updated ones

    @api.onchange("move_ids_without_package")
    def _onchange_category_ids(self):
        self._update_category_ids()
