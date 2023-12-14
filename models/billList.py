from odoo import api, fields, models


class ArchiveList(models.Model):
    _name = 'customer.bill'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Bill Type"

    user_id = fields.Many2many(
        string='User',
        comodel_name='customer.account',
    )
    type = fields.Char(string = "Tên hóa đơn")
    total = fields.Char(string = "Số tiền cần trả")
    status = fields.Selection([('store', 'Chưa thanh toán'),('sended','Đã thanh toán')],string = "Trạng thái")
