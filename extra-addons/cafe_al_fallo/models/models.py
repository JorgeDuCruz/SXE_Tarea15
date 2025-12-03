# -*- coding: utf-8 -*-

from odoo import models, fields, api


class cafe_al_fallo(models.Model):
    _name = 'cafe_al_fallo.cafe_al_fallo'
    _description = 'Lista del nivel de sueno del alumno y su bebida recomendada'

    Alumno = fields.Char(required = True)
    nivel_sueno = fields.Integer(
        string='Nivel de Sueno (1-10)',
        required=True,
        default=1,
        help="Indica qué tan dormido está el alumno, de 1 (poco) a 10 (máximo).",
    )
    bebida_recomendada = fields.Char(compute="_calcularBebida", store=True)

    @api.depends('nivel_sueno')
    def _calcularBebida(self):
        for record in self:
            nivel = record.nivel_sueno

            if nivel<1:
                record.nivel_sueno = 1
                nivel = 1
            elif nivel>10:
                record.nivel_sueno = 10
                nivel = 10

            if nivel >= 1 and nivel <= 3:
                record.bebida_recomendada = "Café con leche"
            elif nivel >= 4 and nivel <= 6:
                record.bebida_recomendada = "Café solo largo"
            elif nivel >= 7 and nivel <= 9:
                record.bebida_recomendada = "Café solo larguísimo"
            elif nivel == 10:
                record.bebida_recomendada = "Inyección de adrenalina (¡Máximo Sueno!)"
            else:
                record.bebida_recomendada = "Nivel de sueno fuera del rango (1-10)"

