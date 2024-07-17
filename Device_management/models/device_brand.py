from odoo import api, fields, models




class DeviceBrand(models.Model):
    _name = "device.brand"
    _description = "Device Brand"

    name = fields.Char(string='Name', required=True, unique=True)
    device_models_ids = fields.One2many('device.model','device_brand_id', string='Device Models')
