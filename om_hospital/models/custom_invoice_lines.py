from odoo import api, fields, models




class CustomInvoiceLines(models.Model):
    _name = "custom.invoice.lines"
    _description = "Custom Invoice Lines"

    account_id = fields.Many2one('account.move')
    product_id = fields.Many2one('product.template', string='Product')
    name = fields.Char(string='Label')
    quantity = fields.Float(string='Quantity')
    price_unit = fields.Float(string='Price')
    # tax_id = fields.
    # price_subtotal = fields.Monetary(string='Subtotal')

