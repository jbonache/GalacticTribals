# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Player(models.Model):
    _name = 'galactic_tribals.player'
    _description = 'Player Model for Galactic Tribals'

    name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

class Tribu(models.Model):
    _name = 'galactic_tribals.tribu'
    _description = 'Tribu Model for Galactic Tribals'

    name = fields.Char()

class Planeta(models.Model):
    _name = 'galactic_tribals.planeta'
    _description = 'Planeta Model for Galactic Tribals'

    name = fields.Char()

class Recurs(models.Model):
    _name = 'galactic_tribals.recurs'
    _description = 'Recurs Model for Galactic Tribals'

    name = fields.Char()

class Construccio(models.Model):
    _name = 'galactic_tribals.construccio'
    _description = 'Construccio Model for Galactic Tribals'

    name = fields.Char()

class Nau(models.Model):
    _name = 'galactic_tribals.nau'
    _description = 'Nau Model for Galactic Tribals'

    name = fields.Char()

class Batalla(models.Model):
    _name = 'galactic_tribals.batalla'
    _description = 'Batalla Model for Galactic Tribals'

    name = fields.Char()

class Alianza(models.Model):
    _name = 'galactic_tribals.alianza'
    _description = 'Alianza Model for Galactic Tribals'

    name = fields.Char()