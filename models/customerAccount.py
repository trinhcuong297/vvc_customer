from odoo import api, fields, models


class CustomerAccount(models.Model):
    _name = 'customer.account'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Customer Type"

    name = fields.Char(string = "Tên")
    phone = fields.Char(string = "Số điện thoại")
    homeLocation = fields.Char(string = "Vị trí căn hộ")
    project = fields.Many2one(string = "Dự án", comodel_name='project.project')
    archiveNeeded = fields.Integer(string = "Số hàng chưa nhận", compute='_compute_archive_needed' )
    billNeeded = fields.Integer(string = "Số hóa đơn chưa thanh toán")
    errorNum = fields.Integer(string = "Số lỗi báo cáo")
    email = fields.Char(string = "Email đăng nhập")
    password = fields.Char(string = "Mật khẩu")

    def _compute_archive_needed(self):
        for record in self:
            record.archive_needed = self.env['customer.archive'].search_count(['user_id','child_of',record.id])