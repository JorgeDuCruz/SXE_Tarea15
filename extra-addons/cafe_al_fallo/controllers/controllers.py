# -*- coding: utf-8 -*-
from odoo import http


class CafeAlFallo(http.Controller):
    @http.route('/cafe_al_fallo/cafe_al_fallo', auth='public')
    def index(self, **kw):
       return "Hello, world"

    @http.route('/cafe_al_fallo/cafe_al_fallo/objects', auth='public')
    def list(self, **kw):
       return http.request.render('cafe_al_fallo.listing', {
           'root': '/cafe_al_fallo/cafe_al_fallo',
           'objects': http.request.env['cafe_al_fallo.cafe_al_fallo'].search([]),
        })

    @http.route('/cafe_al_fallo/cafe_al_fallo/objects/<model("cafe_al_fallo.cafe_al_fallo"):obj>', auth='public')
    def object(self, obj, **kw):
        return http.request.render('cafe_al_fallo.object', {
            'object': obj
        })

