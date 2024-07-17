from odoo import models, fields

class DeviceAttributeAssignment(models.Model):
    _name = 'device.attribute.assignment'
    _description = 'Device Attribute Assignment'
    # _rec_name = 'device_id'  # Optional: set the display name for records
    _sql_constraints = [
        ('unique_device_attribute',
         'unique(device_id, attribute_id)',
         'Each device can only have one value for each attribute!'
        )
    ]

    device_id = fields.Many2one('device.device', string="Device", required=True)
    device_attribute_id = fields.Many2one('device.attribute', string="Device Attribute", required=True)
    device_attribute_value_id = fields.Many2one('device.attribute.value', string="Device Attribute Value",required=True)

