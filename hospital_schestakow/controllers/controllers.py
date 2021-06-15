# -*- coding: utf-8 -*-
# from odoo import http


# class HospitalSchestkow(http.Controller):
#     @http.route('/hospital_schestkow/hospital_schestkow/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hospital_schestkow/hospital_schestkow/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hospital_schestkow.listing', {
#             'root': '/hospital_schestkow/hospital_schestkow',
#             'objects': http.request.env['hospital_schestkow.hospital_schestkow'].search([]),
#         })

#     @http.route('/hospital_schestkow/hospital_schestkow/objects/<model("hospital_schestkow.hospital_schestkow"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hospital_schestkow.object', {
#             'object': obj
#         })
