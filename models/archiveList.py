from odoo import api, fields, models


class ArchiveList(models.Model):
    _name = 'customer.archive'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Archive Type"

    # user_id = fields.Many2one(
    #     string='User',
    #     comodel_name='customer.account',
    # )
    name = fields.Char(string = "Tên người nhận")
    phone = fields.Char(string = "Số điện thoại nhận")
    homeLocation = fields.Char(string = "Vị trí căn hộ nhận")
    # project = fields.Many2one(string = "Dự án", comodel_name='project.project')
    inputURL = fields.Char(string = "Link hình ảnh nhận hàng")
    outputURL = fields.Char(string = "Link hình ảnh trả hàng")
    status = fields.Selection([('store', 'Đã nhận'),('sended','Đã trả')],string = "Trạng thái")
