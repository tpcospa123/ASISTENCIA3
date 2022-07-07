# -*- coding: utf-8 -*-
# from odoo import http


# class TimeCl(http.Controller):
#     @http.route('/time_cl/time_cl/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/time_cl/time_cl/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('time_cl.listing', {
#             'root': '/time_cl/time_cl',
#             'objects': http.request.env['time_cl.time_cl'].search([]),
#         })

#     @http.route('/time_cl/time_cl/objects/<model("time_cl.time_cl"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('time_cl.object', {
#             'object': obj
#         })
