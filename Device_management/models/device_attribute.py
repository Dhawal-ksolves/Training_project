from odoo import api, fields, models




class DeviceAttribute(models.Model):
    _name = "device.attribute"
    _description = "Device Attribute"

    name = fields.Char(string='Name', required=True, unique=True)
    device_type_id = fields.Many2one('device.type', string='Device Type', required=True)
    required = fields.Boolean(string='Required')
    # device_attribute_value_ids = fields.One2many('device.attribute.value', 'attribute_id', string='Attribute Values')

    device_attribute_value_ids = fields.One2many('device.attribute.value', 'device_attribute_id', string="Device Attribute Values")
