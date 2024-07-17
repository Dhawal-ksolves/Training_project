from odoo import api, models, fields

class HospitalBill(models.Model):
    _name = 'hospital.bill'
    _description = 'Hospital Bill'

    name = fields.Char(string='Name of patient')
    patient_id = fields.Many2one('hospital.patient', string='patient name', required = False)
    age_d = fields.Integer(string='Age_D')
    bill1 = fields.Integer(string='bill1')
    bill2 = fields.Integer(string='bill2')
    total = fields.Integer(string='Total bill' , compute='calculate')



    @api.depends('bill1','bill2')
    def calculate(self):
        for record in self:
            total1 = 0
            if record.bill1:
                total1 = total1 + record.bill1
            if record.bill2:
                total1 = total1 + record.bill2
            record.total = total1