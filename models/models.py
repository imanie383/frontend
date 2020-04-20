u"""Modelo Principal."""

# libreria odoo web
from odoo import api, models, fields


class Teacher(models.Model):
    """Clase primaria para la tabla teacher.

    Los modelos son en singular
    Para borrar un modelo que se creo por error es en las tablas
    ir_model_data e ir_model

    """

    _name = 'academy.teacher'
    # se creo la tabla academy_teacher
    name = fields.Char(string='Name')
    biography = fields.Html(string='biography')
