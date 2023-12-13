from odoo import api, fields, models


class ArchiveList(models.Model):
    _name = 'customer.error'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Error Type"

    user_id = fields.Many2one(
        string='Người báo lỗi',
        comodel_name='customer.account',
    )
    errLocation = fields.Char(string = "Vị trí báo lỗi")
    desc = fields.Char(string = "Mô tả")
    imgURL = fields.Char(string = "Link ảnh mô tả")
    status = fields.Selection([('store', 'Chưa xử lý'),('sended','Đã xử lý')],string = "Trạng thái")
