from odoo import api, fields, models


class billList(models.Model):
    _name = 'customer.billList'
    _description = "Customer Bill list"

    name = fields.Char(string = "Tên")
    
