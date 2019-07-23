# -*- coding: utf-8 -*-
from odoo import http

# class NoPurchaseRule(http.Controller):
#     @http.route('/no_purchase_rule/no_purchase_rule/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/no_purchase_rule/no_purchase_rule/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('no_purchase_rule.listing', {
#             'root': '/no_purchase_rule/no_purchase_rule',
#             'objects': http.request.env['no_purchase_rule.no_purchase_rule'].search([]),
#         })

#     @http.route('/no_purchase_rule/no_purchase_rule/objects/<model("no_purchase_rule.no_purchase_rule"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('no_purchase_rule.object', {
#             'object': obj
#         })