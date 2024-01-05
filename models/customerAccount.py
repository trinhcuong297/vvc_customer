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

class CustomerAccount(models.Model):
    _name = 'customer.account'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Customer Type"

    name = fields.Char(string = "Họ và tên")
    birthday = fields.Date(string = "Ngày sinh")
    phone = fields.Char(string = "Số điện thoại")
    email = fields.Char(string = "Email")
    gender = fields.Selection([('man', 'Nam'),('woman','Nữ'),('noinfo','Không xác định')],string = "Giới tính")
    IDCard = fields.Char(string = "Số CMND/Căn cước")
    studyLevel = fields.Char(string = "Trình độ học vấn")
    job = fields.Char(string = "Nghề nghiệp")
    elevatorCard = fields.Char(string = "Thẻ thang máy")
    isCompany = fields.Boolean(string='Khách hàng doanh nghiệp?')
    password = fields.Char(string = "Mật khẩu")
    archiveCount = fields.Integer(string='Đơn hàng chưa nhận',compute='_compute_archiveCount' )
    billCount = fields.Integer(string='Hóa đơn chưa đóng',compute='_compute_billCount' )
    errorCount = fields.Integer(string='Số báo lỗi',compute='_compute_errorCount' )
        
    def _compute_archiveCount(self):
        for record in self:
            record.archiveCount = self.env['customer.archive'].search_count([('user_id','=',record.id),('status','=',"store")])
    
    def _compute_billCount(self):
        for record in self:
            record.billCount = self.env['customer.bill'].search_count([('user_id','=',record.id),('status','=',"store")])

    def _compute_errorCount(self):
        for record in self:
            record.errorCount = self.env['customer.error'].search_count([('user_id','=',record.id)])
    

    ground_ids = fields.Many2many(
        string='Mã mặt bằng',
        comodel_name='customer.ground',
    )

    building = fields.Many2one(string = "Tòa nhà", comodel_name='customer.building',related='ground_ids.building')
    block = fields.Many2one(string = "Block", comodel_name='customer.block',related='ground_ids.block')
    
    partner_id = fields.Char(string='')

# @api.constrains('ground_ids')
# def check_duplicate_customer(self):
#    for account in self:
#         if account.ground_ids:
#             if self.search([('ground_ids', '=', account.ground_ids), ('ground_ids','!=', account.ground_ids)], limit=1):
#                 raise ValueError(('The client reference number already exists in the system. Please enter a unique value.'))


class Building(models.Model):
    _name = 'customer.building'
    _description = "Building"

    name = fields.Char(string = "Tên tòa nhà")
    location = fields.Char(string = "Vị trí tòa nhà")

class Block(models.Model):
    _name = 'customer.block'
    _description = "Block"

    name = fields.Char(string = "Tên block")
    building = fields.Many2one(string = "Tòa nhà", comodel_name='customer.building')

class Ground(models.Model):
    _name = 'customer.ground'
    _description = "Mặt bằng"

    name = fields.Char(string = "Mã mặt bằng")
    waterClock = fields.Char(string = "Mã đồng hồ nước")
    waterClockQrCode = fields.Binary('QR Đồng hồ nước', compute='_generate_w_qr')
    elecClock = fields.Char(string = "Mã đồng hồ điện")
    elecClockQrCode = fields.Binary('QR Đồng hồ điện', compute='_generate_e_qr')
    stage = fields.Char(string = "Số tầng")
    size = fields.Float(string = "Diện tích mặt bằng (m2)")
    block = fields.Many2one(string = "Block", comodel_name='customer.block')
    building = fields.Many2one(string = "Tòa nhà", comodel_name='customer.building', related='block.building')

    def _generate_w_qr(self):
       for rec in self:
           if qrcode and base64:
               qr = qrcode.QRCode(
                   version=1,
                   error_correction=qrcode.constants.ERROR_CORRECT_L,
                   box_size=3,
                   border=4,
               )
               qr.add_data(rec.waterClock)
               qr.make(fit=True)
               img = qr.make_image()
               temp = BytesIO()
               img.save(temp, format="PNG")
               qr_image = base64.b64encode(temp.getvalue())
               rec.update({'waterClockQrCode':qr_image})
           else:
               raise UserError(_('Necessary Requirements To Run This Operation Is Not Satisfied'))
    
    def _generate_e_qr(self):
       for rec in self:
           if qrcode and base64:
               qr = qrcode.QRCode(
                   version=1,
                   error_correction=qrcode.constants.ERROR_CORRECT_L,
                   box_size=3,
                   border=4,
               )
               qr.add_data(rec.elecClock)
               qr.make(fit=True)
               img = qr.make_image()
               temp = BytesIO()
               img.save(temp, format="PNG")
               qr_image = base64.b64encode(temp.getvalue())
               rec.update({'elecClockQrCode':qr_image})
           else:
               raise UserError(_('Necessary Requirements To Run This Operation Is Not Satisfied'))
               
class TypeQLVHFee(models.Model):
    _name = 'customer.typeqlvhfee'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Loại phí QLVH"

    name = fields.Char(string='Loại', track_visibility='onchange')
    cost = fields.Float(string='Giá', track_visibility='onchange')
    building = fields.Many2one(string = "Tòa nhà", comodel_name='customer.building', track_visibility='onchange')

class TypeElecFee(models.Model):
    _name = 'customer.typeelecfee'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Loại phí Điện"

    name = fields.Char(string='Loại', track_visibility='onchange')
    cost = fields.Float(string='Giá', track_visibility='onchange')
    building = fields.Many2one(string = "Tòa nhà", comodel_name='customer.building', track_visibility='onchange')

class TypeWaterFee(models.Model):
    _name = 'customer.typewaterfee'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Loại phí nước"

    name = fields.Char(string='Loại', track_visibility='onchange')
    cost = fields.Float(string='Giá', track_visibility='onchange')
    building = fields.Many2one(string = "Tòa nhà", comodel_name='customer.building', track_visibility='onchange')

class TypeCarFee(models.Model):
    _name = 'customer.typecarfee'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Loại phí xe"

    name = fields.Char(string='Loại', track_visibility='onchange')
    cost = fields.Float(string='Giá', track_visibility='onchange')
    building = fields.Many2one(string = "Tòa nhà", comodel_name='customer.building', track_visibility='onchange')
