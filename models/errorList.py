from odoo import api, fields, models


class ArchiveList(models.Model):
    _name = 'customer.error'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Error Type"

    name = fields.Char(string = "Người báo lỗi")
    errLocation = fields.Char(string = "Vị trí báo lỗi")
    desc = fields.Char(string = "Mô tả")
    # inputTime = fields.Char(string = "Thời gian nhận")
    # outputTime = fields.Char(string = "Thời gian trả")
    status = fields.Selection([('store', 'Chưa xử lý'),('sended','Đã xử lý')],string = "Trạng thái")
