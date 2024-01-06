from odoo import api, fields, models
from odoo.exceptions import UserError
import datetime

class QrMonitor(models.Model):
    _name = 'customer.qr'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "QR monitor"

    qrCodeScan = fields.Char(string='qrCodeScan', required=True)
    timeScan = fields.Datetime(string='Thời gian ghi', default=lambda self: fields.Datetime.to_string(datetime.datetime.now()), readonly=True )
    invokeTime = fields.Date(
        string='field_name',
        default=fields.Date.context_today,
    )
    
    type = fields.Selection(
        string='Loại',
        selection=[('water', 'Chỉ số nước'), ('elec', 'Chỉ số điện')],
        default = 'water',
        readonly=True
    )
    monthPay = fields.Selection(
        string='Chốt số tháng',
        selection=[('1', 'Tháng 1'), ('2', 'Tháng 2'), ('3', 'Tháng 3'), ('4', 'Tháng 4'),
                          ('5', 'Tháng 5'), ('6', 'Tháng 6'), ('7', 'Tháng 7'), ('8', 'Tháng 8'), 
                          ('9', 'Tháng 9'), ('10', 'Tháng 10'), ('11', 'Tháng 11'), ('12', 'Tháng 12'), ],
        
        default=lambda self: str(datetime.date.today().month)
    )
    yearPay = fields.Char(string='Chốt số năm',default=lambda self: str(datetime.date.today().year))
    name = fields.Char(string="Tiêu đề", compute='_compute_title')
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

    status = fields.Selection(
        string='Trạng thái',
        selection=[('draf', 'Ghi nhận'), ('ok', 'Chấp nhận'), ('err', 'Hủy')],
        default = 'draf',
        track_visibility='onchange'
    )

    def getGround(self):
        for rec in self:
            allGround = self.env['customer.ground']
            rec.ground_ids = allGround.search([('waterClock','=',rec.qrCodeScan)], limit = 1)
            if rec.ground_ids:
                rec.type = 'water'
            else:
                rec.ground_ids = allGround.search([('elecClock','=',rec.qrCodeScan)], limit = 1)
                rec.type = 'elec'

    @api.constrains('status')
    def check_duplicate_qr_res(self):
        for rec in self:
            if self.search([('monthPay', '=', rec.monthPay),('type','=', rec.type), ('yearPay','=', rec.yearPay), ('qrCodeScan','=', rec.qrCodeScan), ('id','!=', rec.id)], limit=1):
                raise UserError(('The record already exists in the system. Please enter a unique value.'))

    def _compute_title(self):
        for record in self:
            record.title = record.type + " " + record.monthPay + "/"+ record.yearPay











    
