from odoo import api, models, fields

import logging

_logger = logging.getLogger(__name__)

class HospitalCommands(models.Model):
    _name = 'hospital.commands'
    _description = 'Hospital Commands'

    name = fields.Char(string="name")
    address = fields.Char(string="address")
    test_ids = fields.One2many("hospital.table", "test_id" , string="test")

    _sql_constraints = [
        ('name', 'unique (name)', "Tag name already exists !"),
    ]

    # @api.multi
    def Cammand0(self):
        rec = [(0,0, {'name':self.name, 'address':self.address, 'test_id':self.id})]
        self.test_ids = rec

    def Cammand1(self):
        if self.test_ids:
            last_test = self.test_ids[-1]
            rec = [(1, last_test.id, {'name': 'Writed', 'address': 'addresswrited'})]

            self.test_ids = rec

    def Cammand2(self):
        if self.test_ids:
            last_test = self.test_ids[-1]
            rec = [(2, last_test.id)]
            self.test_ids = rec

    def Cammand3(self):
        if self.test_ids:
            last_test = self.test_ids[-1]
            rec = [(3, last_test.id)]
            self.test_ids = rec

    def Cammand4(self):
        if self.test_ids:
            last_test = self.test_ids[-1]
            rec = [(4, last_test.id)]
            self.test_ids = rec

    def Cammand5(self):
        if self.test_ids:
            # last_test = self.test_ids[-1]
            rec = [(5)]
            self.test_ids = rec

    def Cammand6(self):
        if self.test_ids:
            last_test = self.test_ids[-1]
            rec = [(6,0, [last_test.id])]
            self.test_ids = rec
