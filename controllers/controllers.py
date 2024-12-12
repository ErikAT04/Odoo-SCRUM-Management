# -*- coding: utf-8 -*-
# from odoo import http


# class Manageerik(http.Controller):
#     @http.route('/manageerik/manageerik', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/manageerik/manageerik/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('manageerik.listing', {
#             'root': '/manageerik/manageerik',
#             'objects': http.request.env['manageerik.manageerik'].search([]),
#         })

#     @http.route('/manageerik/manageerik/objects/<model("manageerik.manageerik"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('manageerik.object', {
#             'object': obj
#         })
