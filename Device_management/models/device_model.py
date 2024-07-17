from odoo import api, fields, models




class DeviceModel(models.Model):
    _name = "device.model"
    _description = "Device Model"

    # _rec_name = 'name'  # Optional: set the display name for records

    name = fields.Char(string="Name", required=True, unique=True)
    device_type_id = fields.Many2one('device.type', string="Device Type", required=True)
    device_brand_id = fields.Many2one('device.brand', string="Device Brand", required=True)
