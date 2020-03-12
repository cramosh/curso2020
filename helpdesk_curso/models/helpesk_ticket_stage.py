# -*- coding: utf-8 -*-
# Copyright 2020 See manifest
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from odoo import models, fields, api, _

class HelpdeskTicketStage(models.Model):

    _name = 'helpdesk.ticket.stage'
    _description = 'Ticket Stage'

    name = fields.Char(
        string='Name',
        required=True
    )
