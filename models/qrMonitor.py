from odoo import api, fields, models
import datetime

class QrMonitor(models.Model):
    _name = 'customer.qr'
    _description = "QR monitor"

    qrCodeScan = fields.Char(string='qrCodeScan')
    timeScan = fields.Datetime(string='Thời gian ghi', default=lambda self: fields.Datetime.to_string(datetime.datetime.now()) )
    
