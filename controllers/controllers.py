# -*- coding: utf-8 -*-
from odoo import http

# class HeureSup(http.Controller):
#     @http.route('/heure_sup/heure_sup/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/heure_sup/heure_sup/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('heure_sup.listing', {
#             'root': '/heure_sup/heure_sup',
#             'objects': http.request.env['heure_sup.heure_sup'].search([]),
#         })

#     @http.route('/heure_sup/heure_sup/objects/<model("heure_sup.heure_sup"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('heure_sup.object', {
#             'object': obj
#         })