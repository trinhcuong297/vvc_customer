from odoo import api, fields, models


class ArchiveList(models.Model):
    _name = 'customer.archive'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Archive Type"

    user_id = fields.Many2one(
        string='User',
        related='customer.account',
    )
    name = fields.Char(string = "Tên người nhận")
    phone = fields.Char(string = "Số điện thoại nhận")
    homeLocation = fields.Char(string = "Căn hộ nhận")
    project = fields.Many2one(string = "Dự án", comodel_name='project.project')
    inputImage = fields.Image(string = "Hình ảnh nhận hàng")
    outputImage = fields.Image(string = "Hình ảnh trả hàng")
    status = fields.Selection([('store', 'Đã nhận'),('sended','Đã trả')],string = "Trạng thái")