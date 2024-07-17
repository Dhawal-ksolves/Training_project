from odoo import models, fields

class HREmployee(models.Model):
    _inherit = 'hr.employee'

    is_teacher = fields.Boolean(string='Is a Teacher', default=False)
    subject = fields.Char(string='Subject')
    class_ids = fields.One2many('school.class', 'teacher_id', string='Classes')




class SchoolClass(models.Model):
    _name = 'school.class'
    _description = 'Class'

    name = fields.Char(string='Class Name', required=True)
    teacher_id = fields.Many2one('hr.employee', string='Teacher')