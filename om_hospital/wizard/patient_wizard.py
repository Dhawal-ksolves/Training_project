from odoo import models, fields, api

class HospitalPatientWizard(models.TransientModel):
    _name = 'hospital.patient.wizard'
    _description = 'Patient Wizard'

    patient_id = fields.Many2one('hospital.patient', string='Patient')
    name = fields.Char(string='Name')
    discharge = fields.Boolean(string='Discharge', default=False)
    age = fields.Integer(string='Age')
    is_child = fields.Boolean(string='Is Child?')
    notes = fields.Text(string='Notes')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('others', 'Others')], string='Gender')
    doctor_id = fields.Many2one('hospital.doctor', string='Doctor Name')
    speciality = fields.Char(string='Speciality', related='doctor_id.speciality')
    medicine_id = fields.One2many('hospital.medicine', 'connecting_field', string='Medicine')
    country_id = fields.Many2many('res.country', string="Countries")

    @api.model
    def default_get(self, fields):
        res = super(HospitalPatientWizard, self).default_get(fields)
        active_id = self.env.context.get('active_id')
        if active_id:
            patient = self.env['hospital.patient'].browse(active_id)
            medicine_vals = []
            for rec in patient.medicine_id:
                medicine_vals.append((0, 0, {
                    'name': rec.name,
                    'product_id':rec.product_id}))

            res.update({
                'patient_id': patient.id,
                'name': patient.name,
                'discharge': patient.discharge,
                'age': patient.age,
                'is_child': patient.is_child,
                'notes': patient.notes,
                'gender': patient.gender,
                'doctor_id': patient.doctor_id.id,
                'speciality': patient.speciality,
                'medicine_id': medicine_vals
                # 'country_id': [(0, 0, patient.country_id.ids)],
            })
        return res


    def show_bills(self):
        # Implement your logic to show bills or any other functionality
        pass



class HospitalMedicine1(models.TransientModel):
    _name = "hospital.medicine1"
    _description = "Medicine records"

    connecting_field1 = fields.Many2one('hospital.patient.wizard', string='medicine ID')
    name = fields.Char(string='name')
    product_id = fields.Many2one('product.product', string='product')