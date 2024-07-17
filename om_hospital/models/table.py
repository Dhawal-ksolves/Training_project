from odoo import api, models, fields


class HospitalTable(models.Model):
    _name = 'hospital.table'
    _description = 'Hospital Table'

    name = fields.Char(string="name")
    address = fields.Char(string="address")

    test_id = fields.Many2one("hospital.commands",string="test_ids")