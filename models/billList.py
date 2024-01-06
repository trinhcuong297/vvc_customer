from odoo import api, fields, models


class BillList(models.Model):
    _name = 'customer.bill'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Bill Type"

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
    type = fields.Char(string = "Tên hóa đơn")
    total = fields.Char(string = "Số tiền cần trả")
    status = fields.Selection([('store', 'Chưa thanh toán'),('sended','Đã thanh toán')],string = "Trạng thái")

class monthFeeTable(models.Model):
    _name = 'customer.monthfee'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Month Fee Table"

    name = fields.Char(string = "Tháng thu phí")



class ServiceFeeTable(models.Model):
    _name = 'customer.servicefeetable'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Service Fee Table"

    name = fields.Char(string = "Tên biểu phí", default='Phí dịch vụ', readonly=True)
    ground_ids = fields.Many2one(
        string='Mã mặt bằng',
        comodel_name='customer.ground'
    )
    block = fields.Many2one(string = "Block", comodel_name='customer.block', related='ground_ids.block')
    building = fields.Many2one(string = "Tòa nhà", comodel_name='customer.building', related='ground_ids.building')
    type = fields.Char(string='Loại', related='ground_ids.typeQLVH.name')
    cost = fields.Integer(string='Đơn giá (VND)', related='ground_ids.typeQLVH.cost')
    size = fields.Float(string = "Diện tích mặt bằng (m2)", related='ground_ids.size')
    total = fields.Float(string = "Số tiền cần trả", compute='_compute_total')
    title = fields.Many2one(string = "Tiêu đề", comodel_name='customer.monthfee')
    status = fields.Selection([('store', 'Chưa phát hành hóa đơn'),('sended','Đã phát hành hóa đơn')],string = "Trạng thái")
    
    def _compute_total(self):
        for record in self:
            record.total = record.cost * record.size

class WaterFeeTable(models.Model):
    _name = 'customer.waterfeetable'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Water Fee Table"

    name = fields.Char(string = "Tên biểu phí", default='Phí nước', readonly=True)
    ground_ids = fields.Many2one(
        string='Mã mặt bằng',
        comodel_name='customer.ground'
    )
    block = fields.Many2one(string = "Block", comodel_name='customer.block', related='ground_ids.block')
    title = fields.Many2one(string = "Tiêu đề", comodel_name='customer.monthfee')
    building = fields.Many2one(string = "Tòa nhà", comodel_name='customer.building', related='ground_ids.building')
    size = fields.Float(string = "Diện tích mặt bằng (m2)", related='ground_ids.size')
    oldWater = fields.Many2one(string="Phiếu nước tháng trước", comodel_name="customer.qr", domain=[('type','=','water'),('status','=','ok')])
    oldNumWater = fields.Float(string = "Chỉ số nước trước(m3)", related='oldWater.water')
    newWater = fields.Many2one(string="Phiếu nước tháng này", comodel_name="customer.qr", domain=[('type','=','water'),('status','=','ok')])
    newNumWater = fields.Float(string = "Chỉ số nước hiện tại(m3)", related='newWater.water')
    waterUsedNum = fields.Float(string = "Số nước tiêu thụ(m3)", compute='_compute_waterUsedNum')
    totalBefore = fields.Float(string = "Số tiền cần trả", compute='_compute_total_before')
    totalVAT = fields.Float(string = "Thuế VAT", compute='_compute_vat')
    totalBVMT = fields.Float(string = "Thuế bảo vệ môi trường", compute='_compute_bvmt')
    total = fields.Float(string = "Số tiền cần trả", compute='_compute_total')
    status = fields.Selection([('store', 'Chưa phát hành hóa đơn'),('sended','Đã phát hành hóa đơn')],string = "Trạng thái")

    type = fields.Char(string='Loại', related='ground_ids.typeWater.name')
    vat = fields.Float(string='VAT (%)', related='ground_ids.typeWater.vat')
    envProtect = fields.Float(string='Thuế bảo vệ môi trường (%)', related='ground_ids.typeWater.envProtect')
    limit1 = fields.Float(string='Bậc 1 (m3)', related='ground_ids.typeWater.limit1')
    cost1 = fields.Integer(string='Giá bậc 1 (VND)', related='ground_ids.typeWater.cost1')
    limit2 = fields.Float(string='Bậc 2 (m3)', related='ground_ids.typeWater.limit2')
    cost2 = fields.Integer(string='Giá bậc 2 (VND)', related='ground_ids.typeWater.cost2')
    limit3 = fields.Float(string='Bậc 3 (m3)', related='ground_ids.typeWater.limit3')
    cost3 = fields.Integer(string='Giá bậc 3 (VND)', related='ground_ids.typeWater.cost3')
    limit4 = fields.Float(string='Bậc 4 (m3)', related='ground_ids.typeWater.limit4')
    cost4 = fields.Integer(string='Giá bậc 4 (VND)', related='ground_ids.typeWater.cost4')
    limit5 = fields.Float(string='Bậc 5 (m3)', related='ground_ids.typeWater.limit5')
    cost5 = fields.Integer(string='Giá bậc 5 (VND)', related='ground_ids.typeWater.cost5')
    limit6 = fields.Float(string='Bậc 6 (m3)', related='ground_ids.typeWater.limit6')
    cost6 = fields.Integer(string='Giá bậc 6 (VND)', related='ground_ids.typeWater.cost6')
    limit7 = fields.Float(string='Bậc 7 (m3)', related='ground_ids.typeWater.limit7')
    cost7 = fields.Integer(string='Giá bậc 7 (VND)', related='ground_ids.typeWater.cost7')
    limit8 = fields.Float(string='Bậc 8 (m3)', related='ground_ids.typeWater.limit8')
    cost8 = fields.Integer(string='Giá bậc 8 (VND)', related='ground_ids.typeWater.cost8')
    limit9 = fields.Float(string='Bậc 9 (m3)', related='ground_ids.typeWater.limit9')
    cost9 = fields.Integer(string='Giá bậc 9 (VND)', related='ground_ids.typeWater.cost9')
    limit10 = fields.Float(string='Bậc 10 (m3)', related='ground_ids.typeWater.limit10')
    cost10 = fields.Integer(string='Giá bậc 10 (VND)', related='ground_ids.typeWater.cost10')
    difType = fields.Char(string='Loại phí khác', related='ground_ids.typeWater.difType')
    difRate = fields.Float(string='Số lượng phí khác (%)', related='ground_ids.typeWater.difRate')
    difAbs = fields.Float(string='Số lượng phí khác (VND)', related='ground_ids.typeWater.difAbs')

    @api.depends('waterUsedNum')
    def _compute_total_before(self):
        for record in self:
            if 0 < record.waterUsedNum <= record.limit1:
                total = (record.waterUsedNum - 0)*record.cost1
            elif record.limit1 < record.waterUsedNum <= record.limit2:
                total = (record.waterUsedNum - record.limit1)*record.cost2 + record.limit1*record.cost1
            elif record.limit2 < record.waterUsedNum <= record.limit3:
                total = (record.waterUsedNum - record.limit2)*record.cost3 + (record.limit2 - record.limit1)*record.cost2 + record.limit1*record.cost1
            elif record.limit3 < record.waterUsedNum <= record.limit4:
                total = (record.waterUsedNum - record.limit3)*record.cost4 + (record.limit3 - record.limit2)*record.cost3 + (record.limit2 - record.limit1)*record.cost2 + record.limit1*record.cost1
            elif record.limit4 < record.waterUsedNum <= record.limit5:
                total = (record.waterUsedNum - record.limit4)*record.cost5 + (record.limit4 - record.limit3)*record.cost4 + (record.limit3 - record.limit2)*record.cost3 + (record.limit2 - record.limit1)*record.cost2 + record.limit1*record.cost1
            elif record.limit5 < record.waterUsedNum <= record.limit6:
                total = (record.waterUsedNum - record.limit5)*record.cost6 + (record.limit5 - record.limit4)*record.cost5 + (record.limit4 - record.limit3)*record.cost4 + (record.limit3 - record.limit2)*record.cost3 + (record.limit2 - record.limit1)*record.cost2 + record.limit1*record.cost1
            elif record.limit6 < record.waterUsedNum <= record.limit7:
                total = (record.waterUsedNum - record.limit6)*record.cost7 + (record.limit6 - record.limit5)*record.cost6 + (record.limit5 - record.limit4)*record.cost5 + (record.limit4 - record.limit3)*record.cost4 + (record.limit3 - record.limit2)*record.cost3 + (record.limit2 - record.limit1)*record.cost2 + record.limit1*record.cost1
            elif record.limit7 < record.waterUsedNum <= record.limit8:
                total = (record.waterUsedNum - record.limit7)*record.cost8 + (record.limit7 - record.limit6)*record.cost7 + (record.limit6 - record.limit5)*record.cost6 + (record.limit5 - record.limit4)*record.cost5 + (record.limit4 - record.limit3)*record.cost4 + (record.limit3 - record.limit2)*record.cost3 + (record.limit2 - record.limit1)*record.cost2 + record.limit1*record.cost1
            elif record.limit8 < record.waterUsedNum <= record.limit9:
                total = (record.waterUsedNum - record.limit8)*record.cost9 + (record.limit8 - record.limit7)*record.cost8 + (record.limit7 - record.limit6)*record.cost7 + (record.limit6 - record.limit5)*record.cost6 + (record.limit5 - record.limit4)*record.cost5 + (record.limit4 - record.limit3)*record.cost4 + (record.limit3 - record.limit2)*record.cost3 + (record.limit2 - record.limit1)*record.cost2 + record.limit1*record.cost1
            elif record.limit9 < record.waterUsedNum <= record.limit10:
                total = (record.waterUsedNum - record.limit9)*record.cost10 + (record.limit9 - record.limit8)*record.cost9 + (record.limit8 - record.limit7)*record.cost8 + (record.limit7 - record.limit6)*record.cost7 + (record.limit6 - record.limit5)*record.cost6 + (record.limit5 - record.limit4)*record.cost5 + (record.limit4 - record.limit3)*record.cost4 + (record.limit3 - record.limit2)*record.cost3 + (record.limit2 - record.limit1)*record.cost2 + record.limit1*record.cost1
            record.totalBefore = total

    def _compute_waterUsedNum(self):
        for record in self:
            record.waterUsedNum = record.newNumWater - record.oldNumWater

    @api.depends('totalBefore')
    def _compute_vat(self):
        for record in self:
            record.totalVAT = record.totalBefore*record.vat/100
    
    @api.depends('totalBefore')
    def _compute_bvmt(self):
        for record in self:
            record.totalBVMT = record.totalBefore*record.envProtect/100

    def _compute_total(self):
        for record in self:
            record.total = record.totalBefore + record.totalVAT + record.totalBVMT

    