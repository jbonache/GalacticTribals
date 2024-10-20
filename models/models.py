# -*- coding: utf-8 -*-
from tokenize import String

from odoo import models, fields, api

class Player(models.Model):
    _name = 'galactic_tribals.player'
    _description = 'Player Model for Galactic Tribals'

    name = fields.Char(string='Nom', required=True)
    email = fields.Char(string='Correu electrònic', required=True)
    register_date = fields.Date(string='Data de registre', required=True)
    level = fields.Integer(string='Nivell')
    battle_points = fields.Integer(string='Punts')
    isActive = fields.Boolean()
    avatar=fields.Image(max_width=100, max_height=100, required=True)

    # Fields per a les Relacions
    tribu = fields.Many2one('galactic_tribals.tribu', ondelete='set null', help='La tribu a la que pertany')
    edificacions = fields.One2many(string='Els meus edificis', comodel_name='galactic_tribals.construccio', inverse_name='player')
    naus = fields.One2many('galactic_tribals.nau', 'player')

    # Fields relationals
    batalles = fields.Many2many('galactic_tribals.batalla', related='tribu.batalles', readonly=True)
    aliances = fields.Many2many('galactic_tribals.alianza', related='tribu.aliances', readonly=True)

class Tribu(models.Model):
    _name = 'galactic_tribals.tribu'
    _description = 'Tribu Model for Galactic Tribals'

    name = fields.Char(string='Nom', required=True)
    home_planet = fields.Char(string='Planeta d\'orige', required=True)
    ability = fields.Char(string='Habilitat', required=True)

    # Fields per a les Relacions
    players = fields.One2many(string='Els meus jugadors',comodel_name='galactic_tribals.player', inverse_name='tribu')
    batalles = fields.Many2many(comodel_name='galactic_tribals.batalla',
                                relation='tribus_batalles',
                                column1='tribu_id',
                                column2='batalla_id')
    aliances = fields.Many2many(comodel_name='galactic_tribals.alianza',
                                relation='tribus_aliances',
                                column1='tribu_id',
                                column2='alianza_id')


class Planeta(models.Model):
    _name = 'galactic_tribals.planeta'
    _description = 'Planeta Model for Galactic Tribals'

    name = fields.Char(string='Nom', required=True)
    environment = fields.Char(string='Entorn', required=True)
    status = fields.Char(string='Estat', required=True)

    # Fields per a les Relacions
    construccions = fields.One2many('galactic_tribals.construccio', 'planeta')
    recursos = fields.One2many(string='Els meus recursos',comodel_name='galactic_tribals.recurs', inverse_name='planeta')


class Recurs(models.Model):
    _name = 'galactic_tribals.recurs'
    _description = 'Recurs Model for Galactic Tribals'

    name = fields.Char(string='Nom', required=True)
    type = fields.Char(string='Tipo', required=True)
    quantity = fields.Char(string='Quantitat disponible', required=True)

    # Fields per a les Relacions
    planeta = fields.Many2one('galactic_tribals.planeta', ondelete='set null', help='El planeta on es troba')

class Construccio(models.Model):
    _name = 'galactic_tribals.construccio'
    _description = 'Construccio Model for Galactic Tribals'

    name = fields.Char(string='Nom', required=True)
    type = fields.Char(string='Tipo', required=True)
    status = fields.Char(string='Estat', required=True)

    # Fields per a les Relacions
    planeta = fields.Many2one('galactic_tribals.planeta', ondelete='set null', help='El planeta on s"ha construit')
    player = fields.Many2one('galactic_tribals.player', ondelete='set null', help='El jugador que l"ha construit')

class Nau(models.Model):
    _name = 'galactic_tribals.nau'
    _description = 'Nau Model for Galactic Tribals'

    name = fields.Char(string='Nom', required=True)
    type = fields.Char(string='Tipo', required=True)
    status = fields.Char(string='Estat', required=True)

    # Fields per a les Relacions
    player = fields.Many2one('galactic_tribals.player', ondelete='set null', help='El seu jugador propietari')

class Batalla(models.Model):
    _name = 'galactic_tribals.batalla'
    _description = 'Batalla Model for Galactic Tribals'

    name = fields.Char(string='Nom', required=True)
    date = fields.Date(string='Data', required=True)
    #guanyador = fields.Char(string='Guanyador', required=True)

    # Fields per a les Relacions
    tribus = fields.Many2many(comodel_name='galactic_tribals.tribu',
                              relation='tribus_batalles',
                              column2='tribu_id',
                              column1='batalla_id')

    # Fields relationals
    guanyador = fields.Many2one('galactic_tribals.tribu', ondelete='set null', help='El guanyador de la batalla')

class Alianza(models.Model):
    _name = 'galactic_tribals.alianza'
    _description = 'Alianza Model for Galactic Tribals'

    name = fields.Char(string='Nom', required=True)
    date = fields.Date(string='Data', required=True)
    status = fields.Char(string='Estat', required=True)

    # Fields per a les Relacions
    tribus = fields.Many2many(comodel_name='galactic_tribals.tribu',
                                relation='tribus_aliances',
                                column2='tribu_id',
                                column1='alianza_id')

