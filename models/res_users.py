
from odoo import fields,models

class ResUsers(models.Model):
    _inherit = 'res.users'

    allowed_categories = fields.Many2many('product.category')

