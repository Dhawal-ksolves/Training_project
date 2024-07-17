from odoo import api, fields, models
from odoo.exceptions import UserError, ValidationError
from odoo import _

import logging

_logger = logging.getLogger(__name__)


# from odoo.tools.translate import _

class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _description = "Patient records"

    name = fields.Char(string='Name')
    discharge = fields.Boolean(string='discharge', default=False)
    age = fields.Integer(string='Age')
    is_child = fields.Boolean(string='Is_child?')
    notes = fields.Text(string='notes')
    gender = fields.Selection([('male','Male'),('female','Female'),('others','Others')],string='Gender')
    doctor_id = fields.Many2one('hospital.doctor', string='Doctor name', required = False)
    speciality = fields.Char(string='speciality', related='doctor_id.speciality')
    user_id = fields.Many2one('res.users', string='User Select', default=lambda self: self.env.user)
    # user_name = fields.Char(string="User Name", readonly=True, default=lambda self: self.env.user.name)


    medicine_id = fields.One2many('hospital.medicine','connecting_field',string='medicine')
    country_id = fields.Many2many('res.country',string="Countries")
    # bill_id = fields.Many2one('hospital.bill', string='Patient_bill' , required = False)
    bill_ids = fields.One2many('hospital.bill', 'patient_id', string='Patient Bills')

    state = fields.Selection([
        ('admit', 'Admit'),
        ('discharge', 'Discharge'),
    ], string='State', default='admit', required=True, tracking=True)

    def action_discharge(self):
        self.ensure_one()
        self.write({'state': 'discharge'})

    def action_admit(self):
        self.ensure_one()
        self.write({'state': 'admit'})

    def action_admit_to_discharge(self):
        self.ensure_one()
        self.write({'state': 'discharge' , 'discharge': True})

    def show_bills(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Bills',
            'view_mode': 'tree,form',
            'res_model': 'hospital.bill',
            'domain': [('patient_id', '=', self.id)],
            'context': "{'create': False}"
        }


    _sql_constraints = [
        ('name', 'unique (name)', "Tag name already exists !"),
    ]






    # def action_check_discharge(self):
    #     for rec in self:
    #         if rec.discharge:
    #             raise ValidationError(_("Patient is Discharged"))
    def action_discharge(self):
        for rec in self:
            rec.discharge = True
            # if rec.discharge:
            #     raise ValidationError(_("Patient is Discharged"))



class HospitalMedicine(models.Model):
    _name = "hospital.medicine"
    _description = "Medicine records"

    connecting_field = fields.Many2one('hospital.patient',string='medicine ID')
    # connecting_field1 = fields.Many2one('hospital.patient.wizard',string='medicine ID')
    name = fields.Char(string='name')
    product_id = fields.Many2one('product.product',string='product')


    # _sql_constraints = [
    #     (
    #         'check_age',
    #         'CHECK (age <= 50)',
    #         'Age should be less than or equal to 50'
    #     ),
    # ]
    # @api.onchange('discharge')
    # def check_discharge(self):
    #     self.discharge = True
    #     for field in self._fields:
    #         if field != 'id':
    #             self._fields[field].readonly = True
    #     self.env.cr.commit()

    # @api.constrains('age')
    # def check_age(self):
    #     for rec in self:
    #         if rec.age and rec.age > 50:
    #             raise ValidationError(_("Age should be less than 50"))