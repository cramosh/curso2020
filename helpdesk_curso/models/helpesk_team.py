# -*- coding: utf-8 -*-
# Copyright 2020 See manifest
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from odoo import models, fields, api, _

class HelpdeskTeam(models.Model):

    _name = 'helpdesk.team'
    _description = 'Team'

    name = fields.Char(
        string='Name',
        required=True
    )
    ticket_ids = fields.One2many(
        string='Tickets',
        comodel_name="helpdesk.ticket",
        inverse_name='team_id'
    )
    user_ids = fields.One2many(
        string='Users',
        comodel_name='res.users',
        inverse_name='helpdesk_team_id'
    )

