try:
   import qrcode
except ImportError:
   qrcode = None
try:
   import base64
except ImportError:
   base64 = None
from io import BytesIO
from odoo import api, fields, models
from odoo.exceptions import UserError
import datetime


class PMQRMonitor(models.Model):
    _name = 'customer.pmqr'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "PM QR Code"

    stage = fields.Char(string = "Tầng", track_visibility='onchange')
    desc = fields.Char(string = "Mô tả", track_visibility='onchange')
    block = fields.Many2one(string = "Block", comodel_name='customer.block', track_visibility='onchange')
    building = fields.Many2one(string = "Tòa nhà", comodel_name='customer.building', related='block.building')
    pmCode = fields.Char(string = "Mã quản lý", track_visibility='onchange')
    pmQRcode = fields.Binary('QR Quản lý', compute='_generate_p_qr')
    
    def _generate_p_qr(self):
       for rec in self:
           if qrcode and base64:
               qr = qrcode.QRCode(
                   version=1,
                   error_correction=qrcode.constants.ERROR_CORRECT_L,
                   box_size=3,
                   border=4,
               )
               qr.add_data(rec.pmCode)
               qr.make(fit=True)
               img = qr.make_image()
               temp = BytesIO()
               img.save(temp, format="PNG")
               qr_image = base64.b64encode(temp.getvalue())
               rec.update({'pmQRcode':qr_image})
           else:
               raise UserError(_('Necessary Requirements To Run This Operation Is Not Satisfied'))
    
class PMC(models.Model):
    _name = 'customer.pmc'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "PMC"

    qrCodeScan = fields.Char(string='qrCodeScan')
    timeScan = fields.Datetime(string='Thời gian ghi', default=lambda self: fields.Datetime.to_string(datetime.datetime.now()), readonly=True )
    pmQR = fields.Many2one(string = "PM Code",comodel_name = 'customer.pmqr', compute='getPMQR')
    building = fields.Many2one(string = "Tòa nhà", comodel_name='customer.building',related='pmQR.building')
    block = fields.Many2one(
        string = "Block", 
        comodel_name='customer.block',
        related='pmQR.block'
    )
    stage = fields.Char(string = "Tầng", related = 'pmQR.stage')
    desc = fields.Char(string = "Mô tả", related = 'pmQR.desc')
    anState = fields.Selection(string = "Đánh giá an ninh", selection=[('ok', 'Đạt'), ('fail', 'Không đạt')])
    anComment = fields.Html(string = "Chi tiết an ninh")
    vsState = fields.Selection(string = "Đánh giá vệ sinh", selection=[('ok', 'Đạt'), ('fail', 'Không đạt')])
    vsComment = fields.Html(string = "Chi tiết vệ sinh")
    ktState = fields.Selection(string = "Đánh giá kĩ thuật", selection=[('ok', 'Đạt'), ('fail', 'Không đạt')])
    ktComment = fields.Html(string = "Chi tiết kĩ thuật")
    

    def getPMQR(self):
        for rec in self:
            allpmQR = self.env['customer.pmqr']
            rec.pmQR = allpmQR.search([('pmCode','=',rec.qrCodeScan)], limit = 1)

