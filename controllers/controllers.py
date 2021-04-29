# -*- coding: utf-8 -*-
# from odoo import http


# class ProdMgmt(http.Controller):
#     @http.route('/prod_mgmt/prod_mgmt/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/prod_mgmt/prod_mgmt/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('prod_mgmt.listing', {
#             'root': '/prod_mgmt/prod_mgmt',
#             'objects': http.request.env['prod_mgmt.prod_mgmt'].search([]),
#         })

#     @http.route('/prod_mgmt/prod_mgmt/objects/<model("prod_mgmt.prod_mgmt"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('prod_mgmt.object', {
#             'object': obj
#         })
