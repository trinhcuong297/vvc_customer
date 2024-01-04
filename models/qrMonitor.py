from odoo import api, fields, models


class QrMonitor(models.Model):
    _name = 'customer.qr'
    _description = "QR monitor"

    qrCodeScan = fields.Char(string='qrCodeScan')
    
    
