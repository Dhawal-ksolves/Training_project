import time

from odoo import api, fields, models, _
from odoo.exceptions import UserError
from odoo.fields import Command
from odoo.tools import float_is_zero


class SaleAdvancePaymentInv(models.TransientModel):
    _inherit = 'sale.advance.payment.inv'
    _description = "Sales Advance Payment Invoice"

    def create_invoices(self):
        res = super(SaleAdvancePaymentInv, self).create_invoices()

        invoices = self.env['account.move'].search([('id', '=', res.get('res_id'))])
        # custom_order_line_ids = []
        product_vals = []
        for rec in self.sale_order_ids.duplicate_line_ids:
            product_vals.append((0, 0, {
                'product_id': rec.product_id.id,
                'name': rec.name,
                'quantity': rec.quantity}))

        invoices.update({
            'invoice_line_customs_ids': product_vals})
        # for invoice in invoices:
        #     for line in invoice.invoice_line_ids:
        #         self.env['custom.invoice.line'].create({
        #             'move_id': invoice.id,
        #             'product_id': line.product_id.id,
        #             'quantity': line.quantity,
        #             # 'price_unit': line.price_unit,
        #             # Add any other necessary fields
        #             # 'custom_field': 'Custom Value',
        #         })
        #     invoice.invoice_line_ids.unlink()
        return res

        # def _prepare_invoice_values(self, order, so_line):
        #     # self.ensure_one()
        #     return {
        #         # **order._prepare_invoice(),
        #         'invoice_line_customs_ids': [
        #             Command.create(
        #                 so_line._prepare_invoice_line(
        #                     name=self._get_down_payment_description(order),
        #                     quantity=1.0,
        #                 )
        #             )
        #         ],
        #
        #     }