# -*- coding: utf-8 -*-

from odoo import models, fields, api

class MrpBom(models.Model):
    _inherit = 'mrp.bom'

    product_tmpl_id = fields.Many2one(
        'product.template', related='product_x_id.product_tmpl_id',store=True,readonly=False,required=False)
    product_x_id = fields.Many2one(
        'product.product', 'Product X Variant')
