from odoo import api, fields, models


class archiveList(models.Model):
    _name = 'customer.archiveList'
    _description = "Customer Archive list"







    # sequence = fields.Integer()
    # path_id = fields.Many2one(
    #     'api.rest.path', required=True, ondelete='cascade')
    # model_id = fields.Many2one(
    #     related="path_id.model_id", readonly=True)
    # field_id = fields.Many2one(
    #     'ir.model.fields', required=True, ondelete='cascade',
    #     domain="["
    #            "('model_id', '=', model_id),"
    #            "]")
    # field_name = fields.Char(
    #     related="field_id.name", readonly=True)
    # description = fields.Char()
    # force_required = fields.Boolean(
    #     related="field_id.required", readonly=True)
    # required = fields.Boolean()
    # default_value = fields.Char()

    # @api.onchange('field_id')
    # def _onchange_field_id(self):
    #     self.required = self.field_id.required

    # @api.onchange('default_value')
    # def _onchange_default_value(self):
    #     if self.default_value:
    #         self.required = False

    # @api.onchange('required')
    # def _onchange_required(self):
    #     if self.default_value:
    #         self.required = False
