from odoo import api, fields, models


class CustomerAccount(models.Model):
    _name = 'customer.account'
    _description = "Customer Type"

    name = fields.Char(string = "Tên")
    phone = fields.Char(string = "Số điện thoại")
    homeLocation = fields.Char(string = "Vị trí căn hộ")
    project = fields.Char(string = "Dự án")
    archiveNeeded = fields.Integer(string = "Số hàng chưa nhận")
    billNeeded = fields.Integer(string = "Số hóa đơn chưa thanh toán")
    errorNum = fields.Integer(string = "Số lỗi báo cáo")
    email = fields.Char(string = "Email đăng nhập")
    password = fields.Char(string = "Mật khẩu")
