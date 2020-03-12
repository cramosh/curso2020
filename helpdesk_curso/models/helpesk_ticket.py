# -*- coding: utf-8 -*-
# Copyright 2020 See manifest
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from odoo import models, fields, api, _
from odoo.exceptions import Warning

class HelpdeskTicket(models.Model):

    _name = 'helpdesk.ticket'
    _description = 'Ticket'

    name = fields.Char(
        string='Name',
        required=True
    )
    description = fields.Text(
        string='Description'
    )
    date_deadline = fields.Datetime(
        string='Date Limit'
    )
    team_id = fields.Many2one(
        string='Team',
        comodel_name='helpdesk.team'
    )
    ticket_stage_id = fields.Many2one(
        string='Stage',
        comodel_name='helpdesk.ticket.stage'
    )
    user_ids = fields.Many2many(
        string='Users',
        comodel_name='res.users',
        relation='helpdesk_ticket_user_rel',
        column1='ticket_id',
        column2='user_id'
    )
    stage_id = fields.Many2one(
        string='Stage',
        comodel_name='helpdesk.ticket.stage'
    )

    def btn_auto_assign(self):
        self.ensure_one()# NOS SEGURAMOS QUE SOLO SE EJECUTE CUANDO SELF TENGA UN REGISTRO
        if self.env.user.id not in self.user_ids.ids:
            self.user_ids = [4, self.env.user.id] #Añadimos un valor a un campo Many2many
        else:
            raise Warning(_('This user is just assigned from task.'))

