from odoo import api, fields, models


class ArchiveList(models.Model):
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
