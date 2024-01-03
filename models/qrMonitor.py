from odoo import api, fields, models


class QrMonitor(models.Model):
    _name = 'customer.qr'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "QR monitor"

    
