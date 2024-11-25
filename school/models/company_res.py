from odoo import fields,models

class ResCompany(models.Model):
    _inherit = 'res.company'

    company = fields.Boolean(string="Allowed Company", default=False)