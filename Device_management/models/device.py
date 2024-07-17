from odoo import api, fields, models



class Device(models.Model):
    _name = "device.device"
    _description = "Device"

    name = fields.Char(string='Name/Serial', required=True,  unique=True)
    shared = fields.Boolean(string='Shared')
    device_type_id = fields.Many2one('device.type', string='Device Type', required=True)
    device_brand_id = fields.Many2one('device.brand', string='Device Brand')
    device_model_id = fields.Many2one('device.model', string='Device Model')
    attributes = fields.Many2many('device.attribute.assignment', string='Attributes')


