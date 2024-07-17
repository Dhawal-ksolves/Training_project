from odoo import api, fields, models
from odoo.exceptions import UserError, ValidationError
from odoo import _



class AccountMoveCustom(models.Model):
    _inherit = 'account.move'

    invoice_line_customs_ids = fields.One2many('custom.invoice.lines','account_id')


