from odoo import api, models, fields

class HospitalDoctor(models.Model):
    _name = 'hospital.doctor'
    _description = 'Hospital Doctor'

    name = fields.Char(string='Name', required=True)
    speciality = fields.Char(string='Specialty')
    gender = fields.Selection([('male','Male'),('female','Female'),('others','Others')],string='Gender')
    age_d = fields.Integer(string='Age_D')


    def show_bills(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Bills',
            'view_mode': 'tree,form',
            'res_model': 'hospital.bill',
            'context': "{'create': True}"
        }


    @api.onchange('gender')
    def onchange_doctor_id(self):
        self.age_d = '00'

            # (self.doctor_id.age_d)