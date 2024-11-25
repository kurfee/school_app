from xml import etree

from odoo import fields, models, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    allowed_company = fields.Boolean(compute="_allowed_company", string="Allowed Company")

    @api.depends('state')
    def _allowed_company(self):
        # compute if the current company is the company that we need to allow
        current_company = self.env.company
        for record in self:
            record.allowed_company = current_company.company


        @api.model
        def _get_view(self, view_id=None, view_type='form', **options):
            arch, view = super()._get_view(view_id, view_type, **options)
            active_company = self.env.company
            if view_type == 'form' and active_company.company:
                for node in arch.xpath("//field[@name='order_line']//field[@name='product_template_id']"):
                    node.set('options', "{'no_create': True, 'no_create_edit': True, 'no_open': True}")
            return arch, view
