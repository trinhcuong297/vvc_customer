from odoo import api, fields, models


class ArchiveList(models.Model):
    _name = 'customer.archive'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Archive Type"

    name = fields.Char(string = "Tên người nhận")
    phone = fields.Char(string = "Số điện thoại nhận")
    homeLocation = fields.Char(string = "Vị trí căn hộ nhận")
    project = fields.Char(string = "Dự án")
    # inputTime = fields.Char(string = "Thời gian nhận")
    # outputTime = fields.Char(string = "Thời gian trả")
    status = fields.Selection([('store', 'Đã nhận'),('sended','Đã trả')],string = "Trạng thái")
