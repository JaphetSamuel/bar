# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class bar(models.Model):
#     _name = 'bar.bar'
#     _description = 'bar.bar'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

from odoo import models, fields

class Article(models.Model):
    _name = 'bar.article'
    _description = 'article vendu dans le bar'

    nom = fields.Char(required=True)
    prix = fields.Integer(required=True)
    description = fields.Text()
    image = fields.Image(default="bar/static/image/default.png")
    rupture_stock = fields.Boolean()
    quantite = fields.Integer(required=True)