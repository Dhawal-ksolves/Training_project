from odoo import models, fields

class DeviceAssignment(models.Model):
    _name = 'device.assignment'
    _description = 'Device Assignment'
    # _rec_name = 'name_code'  # Optional: set the display name for records

    name_code = fields.Char(string='Name / Code', required=True, unique=True)
    device_id = fields.Many2one('device.device', string='Device', required=True)
    employee_id = fields.Many2one('hr.employee', string='Employee', required=True)
    date_start = fields.Date(string='Start Date')
    date_expire = fields.Date(string='Expiration Date')
    state = fields.Selection([
        ('new', 'New'),
        ('draft', 'Draft'),
        ('approved', 'Approved'),
        ('returned', 'Returned'),
        ('rejected', 'Rejected')
    ], string='State', default='new')