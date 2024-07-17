from odoo import api, fields, models
from odoo.exceptions import UserError, ValidationError
from odoo import _



class SaleOrder(models.Model):
    _inherit = "sale.order"

    practice_field = fields.Date(string="Practice", related='')
    practice_field_id = fields.Many2one('res.country',string="Practice1")
    duplicate_line_ids = fields.One2many('new.update', 'order_id')
    tax_total = fields.Float(string='Total')



    total = fields.Float(string='Total Calculation', compute='_compute_tax_total')
    # total_related = fields.Many2one('new.update')



    @api.depends('duplicate_line_ids.price_subtotal')
    def _compute_tax_total(self):
        val = 0
        for rec in self:
            for line in rec.duplicate_line_ids:
                val += line.price_subtotal
            rec.total = val


    def open_wizard(self):
        # self.ensure_one()
        return {
            'name': _('Sale order wizard'),
            'view_mode': 'form',
            'res_model': 'inherit.wizard',
            # 'res_id': self.id,
            # 'view_id': False,
            'target': 'new',
            'type': 'ir.actions.act_window',
        }

class NewUpdate(models.Model):
    _name = "new.update"
    _description = "New Update"

    product_id = fields.Many2one('product.template', string='Product')
    order_id = fields.Many2one('sale.order')
    name = fields.Text(string='Description')
    quantity = fields.Float(string='Total Quantity', compute='_compute_product_uom_qty', store=True , readonly=False)

    unit_price = fields.Float(string='Unit price')
    price_subtotal = fields.Float(string='Subtotal',compute='_compute_price_total')
    # sub_total = fields.Monetary(string='Subtotal')
    # tax_total = fields.Float(string='Total', compute='_compute_tax_totals')
    show_total = fields.Float(string='show_total',compute='_compute_totals')

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

    @api.depends('quantity', 'unit_price')
    def _compute_price_total(self):
        for rec in self:
            rec.price_subtotal = rec.quantity * rec.unit_price


    def _compute_product_uom_qty(self):
        for production in self:
            if production.product_id.uom_id != production.product_uom_id:
                production.product_uom_qty = production.product_uom_id._compute_quantity(production.product_qty, production.product_id.uom_id)
            else:
                production.product_uom_qty = production.product_qty



 # @api.depends('duplicate_line_ids.price_subtotal')
    # def _compute_tax_totals(self):
    #     total = 0
    #     for rec in self:
    #         for line in rec.duplicate_line_ids:
    #             if line.price_subtotal:
    #                 rec.tax_total += line.price_subtotal
    #             else:
    #                 rec.tax_total += 0

    # practice_one_ids = fields.One2many('sale.order.inherit', 'practice_field_id', string="Practice2")

# @api.depends('price_subtotal')
# def _compute_tax_totals(self):
#     for rec in self:
#         rec.tax_total += rec.price_subtotal

# @api.depends('show_total')
# def _compute_totals(self):
#     val = 0
#     for rec in self:
#         rec.tax_total += rec.price_subtotal
#         val += rec.tax_total
#     self.show_total= val