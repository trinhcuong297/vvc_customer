from odoo import api, fields, models


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
    

    username = fields.Char(string = "Tên đăng nhập App", compute='_compute_username' )
    password = fields.Char(string = "Mật khẩu")

    ground_ids = fields.Many2many(
        string='Mã mặt bằng',
        comodel_name='customer.ground',
    )

    building = fields.Many2one(string = "Tòa nhà", comodel_name='customer.building',related='ground_ids.building')
    block = fields.Many2one(string = "Block", comodel_name='customer.block',related='ground_ids.block')
    
    partner_id = fields.Char(string='')

    
    def _compute_username(self):
        for record in self:
            record.username = 'user'+self.ground_ids

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
    stage = fields.Integer(string = "Số tầng")
    size = fields.Float(string = "Diện tích mặt bằng (m2)")
    block = fields.Many2one(string = "Block", comodel_name='customer.block')
    building = fields.Many2one(string = "Tòa nhà", comodel_name='customer.building', related='block.building')

  