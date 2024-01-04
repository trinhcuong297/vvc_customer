from odoo import api, fields, models
import datetime

class QrMonitor(models.Model):
    _name = 'customer.qr'
    _description = "QR monitor"

    qrCodeScan = fields.Char(string='qrCodeScan')
    timeScan = fields.Datetime(string='Thời gian ghi', default=lambda self: fields.Datetime.to_string(datetime.datetime.now()) )
    type = fields.Selection(
        string='Loại',
        selection=[('water', 'Chỉ số nước'), ('elec', 'Chỉ số điện')],
        default = 'water'
    )
    ground_ids = fields.Many2one(
        string='Mã mặt bằng',
        comodel_name='customer.ground',
        readonly=True
    )
    building = fields.Many2one(string = "Tòa nhà", comodel_name='customer.building',related='ground_ids.building')
    block = fields.Many2one(string = "Block", comodel_name='customer.block',related='ground_ids.block')
    recordImage = fields.Image(string = "Hình ảnh minh chứng")

    @api.onchange('qrCodeScan')
    def getGround(self):
        for rec in self:
            allGround = self.env['customer.ground']
            rec.ground_ids = allGround.search([('waterClock','=',rec.qrCodeScan)], limit = 1)












    
