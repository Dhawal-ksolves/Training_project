# hospital/models/appointment.py
from odoo import api, models, fields

class HospitalAppointment(models.Model):
    _name = 'hospital.appointment'
    _description = 'Hospital Appointment'

    patient_ids = fields.Many2many('hospital.patient', string='Patients')
    doctor_ids = fields.Many2many('hospital.doctor', string='Doctors')
