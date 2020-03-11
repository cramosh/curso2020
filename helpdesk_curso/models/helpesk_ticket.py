# -*- coding: utf-8 -*-
# Copyright 2020 See manifest
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from odoo import models, fields, api, _

class HelpdeskTicket(models.Model):

    _name = 'helpdesk.ticket'

    name = fields.Char(
        string='name',
        required=True
    )
    description = fields.Text(
        string='Description'
    )
    date_deadline = fields.Datetime(
        string='Date Limit'
    )
