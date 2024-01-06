from odoo import api, fields, models
import datetime

class QrMonitor(models.Model):
    _name = 'customer.qr'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "QR monitor"

    qrCodeScan = fields.Char(string='qrCodeScan')
    timeScan = fields.Datetime(string='Thời gian ghi', default=lambda self: fields.Datetime.to_string(datetime.datetime.now()), readonly=True )
    type = fields.Selection(
        string='Loại',
        selection=[('water', 'Chỉ số nước'), ('elec', 'Chỉ số điện')],
        default = 'water'
    )
    ground_ids = fields.Many2one(
        string='Mã mặt bằng',
        comodel_name='customer.ground',
        readonly=True,
        compute='getGround',
        track_visibility='onchange'
    )
    building = fields.Many2one(string = "Tòa nhà", comodel_name='customer.building',related='ground_ids.building')
    block = fields.Many2one(string = "Block", comodel_name='customer.block',related='ground_ids.block')
    water = fields.Float(string = "Chỉ số nước(m3)", track_visibility='onchange')
    elec = fields.Float(string = "Chỉ số điện(kW)", track_visibility='onchange')
    recordImage = fields.Image(string = "Hình ảnh minh chứng", track_visibility='onchange')

    constMonth = fields.Selection(
        string='Tháng chốt',
        selection=[('1', '1'), ('2', '2'),('3', '3'),('4', '4'),('5', '5'),('6', '6'),('7', '7'),('8', '8'),('9', '9'),('10', '10'),('11', '11'),('12', '12')]
    )
    constYear = fields.Integer(
        string='Năm chốt'
    )
    
    status = fields.Selection(
        string='Trạng thái',
        selection=[('draf', 'Ghi nhận'), ('checking', 'Kiểm tra'), ('ok', 'Xác nhận')],
        default = 'draf',
        track_visibility='onchange'
    )

    def getGround(self):
        for rec in self:
            allGround = self.env['customer.ground']
            rec.ground_ids = allGround.search([('waterClock','=',rec.qrCodeScan)], limit = 1)












    
