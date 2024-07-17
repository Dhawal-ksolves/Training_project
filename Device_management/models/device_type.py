from odoo import api, fields, models


class DeviceType(models.Model):
    _name = 'device.type'
    _description = 'Device Types'

    name = fields.Char(string='Name', required=True, unique=True)
    code = fields.Char(string='Code', required=True, unique=True)
    sequence_id = fields.Many2one('ir.sequence', string='Sequence')
    device_attribute_ids = fields.One2many('device.attribute', 'device_type_id', string='Device Attributes')
    device_model_ids = fields.One2many('device.model', 'device_type_id', string='Device Models')
    device_ids = fields.One2many('device.device', 'device_type_id', string='Devices')
