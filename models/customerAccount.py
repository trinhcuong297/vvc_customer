from odoo import api, fields, models


class customerAccount(models.Model):
    _name = 'customer.customerAccount'
    _description = "Customer list"

    name = fields.Char(string = "Tên")
    phone = fields.Char(string = "Số điện thoại")
    homeLocation = fields.Char(string = "Vị trí căn hộ")
    project = fields.Char(string = "Dự án")
    # archiveNeeded = fields.Interger(string = "Số hàng chưa nhận")
    # billNeeded = fields.Interger(string = "Số hóa đơn chưa thanh toán")
    # errorNum = fields.Interger(string = "Số lỗi báo cáo")
    email = fields.Char(string = "Email đăng nhập")
    password = fields.Char(string = "Mật khẩu")
