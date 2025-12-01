# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class cafe_al_fallo(models.Model):
#     _name = 'cafe_al_fallo.cafe_al_fallo'
#     _description = 'cafe_al_fallo.cafe_al_fallo'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

