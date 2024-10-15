# -*- coding: utf-8 -*-
from tokenize import String

from odoo import models, fields, api

class Player(models.Model):
    _name = 'galactic_tribals.player'
    _description = 'Player Model for Galactic Tribals'

    name = fields.Char(string='Nom')
    email = fields.Char(string='Correu electrònic')
    register_date = fields.Date(string='Data de registre')
    level = fields.Integer(string='Nivell')
    battle_points = fields.Integer(string='Punts')


class Tribu(models.Model):
    _name = 'galactic_tribals.tribu'
    _description = 'Tribu Model for Galactic Tribals'

    name = fields.Char(String='Nom')
    home_planet = fields.Char(string='Planeta d\'orige')
    ability = fields.Char(string='Habilitat')


class Planeta(models.Model):
    _name = 'galactic_tribals.planeta'
    _description = 'Planeta Model for Galactic Tribals'

    name = fields.Char(String='Nom')
    environment = fields.Char(string='Entorn')
    status = fields.Char(string='Estat')

class Recurs(models.Model):
    _name = 'galactic_tribals.recurs'
    _description = 'Recurs Model for Galactic Tribals'

    name = fields.Char()
    type = fields.Char(string='Tipo')
    quantity = fields.Char(string='Quantitat disponible')

class Construccio(models.Model):
    _name = 'galactic_tribals.construccio'
    _description = 'Construccio Model for Galactic Tribals'

    name = fields.Char()
    type = fields.Char(string='Tipo')
    status = fields.Char(string='Estat')

class Nau(models.Model):
    _name = 'galactic_tribals.nau'
    _description = 'Nau Model for Galactic Tribals'

    name = fields.Char()
    type = fields.Char(string='Tipo')
    status = fields.Char(string='Estat')

class Batalla(models.Model):
    _name = 'galactic_tribals.batalla'
    _description = 'Batalla Model for Galactic Tribals'

    name = fields.Char()
    date = fields.Date(string='Data')
    result = fields.Char(string='Resultat (de la tribu atacant)')

class Alianza(models.Model):
    _name = 'galactic_tribals.alianza'
    _description = 'Alianza Model for Galactic Tribals'

    name = fields.Char()
    date = fields.Date(string='Data')
    status = fields.Char(string='Estat')