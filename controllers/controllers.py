# -*- coding: utf-8 -*-
from odoo import http

# class ProductToMrp(http.Controller):
#     @http.route('/product_to_mrp/product_to_mrp/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/product_to_mrp/product_to_mrp/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('product_to_mrp.listing', {
#             'root': '/product_to_mrp/product_to_mrp',
#             'objects': http.request.env['product_to_mrp.product_to_mrp'].search([]),
#         })

#     @http.route('/product_to_mrp/product_to_mrp/objects/<model("product_to_mrp.product_to_mrp"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('product_to_mrp.object', {
#             'object': obj
#         })