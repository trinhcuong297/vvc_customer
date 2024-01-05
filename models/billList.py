from odoo import api, fields, models


class BillList(models.Model):
    _name = 'customer.bill'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Bill Type"

    user_id = fields.Many2one(
        string='User',
        comodel_name='customer.account',
    )
    name = fields.Char(string = "Tên người nhận", related='user_id.name')
    phone = fields.Char(string = "Số điện thoại nhận", related='user_id.phone')
    ground_ids = fields.Many2many(
        string='Mã mặt bằng',
        comodel_name='customer.ground',
        related='user_id.ground_ids'
    )
    block = fields.Many2one(string = "Block", comodel_name='customer.block', related='user_id.block')
    building = fields.Many2one(string = "Tòa nhà", comodel_name='customer.building', related='user_id.building')
    type = fields.Char(string = "Tên hóa đơn")
    total = fields.Char(string = "Số tiền cần trả")
    status = fields.Selection([('store', 'Chưa thanh toán'),('sended','Đã thanh toán')],string = "Trạng thái")

class monthFeeTable(models.Model):
    _name = 'customer.monthfee'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Month Fee Table"

    name = fields.Char(string = "Tháng thu phí")



class ServiceFeeTable(models.Model):
    _name = 'customer.servicefeetable'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Service Fee Table"

    name = fields.Char(string = "Tên biểu phí", default='Phí dịch vụ', readonly=True)
    ground_ids = fields.Many2one(
        string='Mã mặt bằng',
        comodel_name='customer.ground'
    )
    block = fields.Many2one(string = "Block", comodel_name='customer.block', related='ground_ids.block')
    building = fields.Many2one(string = "Tòa nhà", comodel_name='customer.building', related='ground_ids.building')
    type = fields.Char(string='Loại', related='ground_ids.typeQLVH.name')
    cost = fields.Integer(string='Đơn giá (VND)', related='ground_ids.typeQLVH.cost')
    size = fields.Float(string = "Diện tích mặt bằng (m2)", related='ground_ids.size')
    total = fields.Float(string = "Số tiền cần trả", compute='_compute_total')
    title = fields.Many2one(string = "Tiêu đề", comodel_name='customer.monthfee')
    status = fields.Selection([('store', 'Chưa phát hành hóa đơn'),('sended','Đã phát hành hóa đơn')],string = "Trạng thái")
    
    def _compute_total(self):
        for record in self:
            record.total = record.cost * record.size

