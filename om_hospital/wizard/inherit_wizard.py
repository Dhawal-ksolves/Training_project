from odoo import models, fields, api

class inherit_wizard(models.TransientModel):
    _name = 'inherit.wizard'
    _description = 'Inherit Wizard'

    sale_order_line_ids = fields.One2many('product.details', 'wizard_product_id')

    # product_id = fields.Many2one('product.template',string="Product")
    # description = fields.Text(string="Description")
    # quantity = fields.Float(string="Quantity")

    @api.model
    def default_get(self, fields):
        res = super(inherit_wizard, self).default_get(fields)
        active_id = self.env.context.get('active_id')
        if active_id:
            sale_order = self.env['sale.order'].browse(active_id)
            product_vals = []
            for rec in sale_order.order_line:
                product_vals.append((0, 0, {
                    # 'product_variant': rec.product_id,
                    'product_id': rec.product_template_id,
                    'name': rec.name,
                    'quantity': rec.product_uom_qty,
                    'unit_price': rec.price_unit,
                    'price_subtotal': rec.price_subtotal
                }))

            res.update({
                'sale_order_line_ids': product_vals

            })
        return res

    def action_done(self):
        sale_order_id = self.env.context.get('active_id')
        if sale_order_id:
            sale_order = self.env['sale.order'].browse(sale_order_id)
            sale_order.write({'duplicate_line_ids': [(5, 0, 0)]})
            lines = [(0, 0, {
                # 'product_variant': line.product_id,
                'product_id': line.product_id.id,
                'name': line.name,
                'quantity': line.quantity,
                'unit_price': line.unit_price,
                'price_subtotal': line.price_subtotal,
            }) for line in self.sale_order_line_ids]
            sale_order.write({'duplicate_line_ids': lines})




class Productdetails(models.TransientModel):
    _name = "product.details"
    _description = "product details"

    wizard_product_id = fields.Many2one('inherit.wizard')

    # product_variant = fields.Many2one('product.product', string='Variant')
    product_id = fields.Many2one('product.template', string='Product')
    name = fields.Text(string='Description')
    # quantity = fields.Float(string='Quantity')
    quantity = fields.Float(string='Total Quantity', compute='_compute_product_uom_qty', store='True' ,readonly=False)

    unit_price = fields.Float(string='Unit price')
    price_subtotal = fields.Float(string='Subtotal')

    @api.onchange('product_id')
    def _onchange_product_id(self):
        if self.product_id:
            self.name = self.product_id.name
            self.unit_price = self.product_id.list_price
            self.quantity = 1
        else:
            self.name = ''
            self.unit_price = 0
            self.quantity = 0