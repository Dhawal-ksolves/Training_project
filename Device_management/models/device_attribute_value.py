from odoo import api, fields, models



class DeviceAttributeValue(models.Model):
    _name = 'device.attribute.value'
    _description = 'Device Attribute Value'

    name = fields.Char(string='Value', required=True)
    device_attribute_id = fields.Many2one('device.attribute', string='Attribute')