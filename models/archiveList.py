from odoo import api, fields, models


class ArchiveList(models.Model):
    _name = 'customer.archive'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Archive Type"

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
    inputImage = fields.Image(string = "Hình ảnh nhận hàng")
    outputImage = fields.Image(string = "Hình ảnh trả hàng")
    status = fields.Selection([('store', 'Đã nhận'),('sended','Đã trả')],string = "Trạng thái")