# -*- coding: utf-8 -*-
# Copyright 2020 See manifest
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from odoo import models, fields, api, _

class ResUsers(models.Model):

    _inherit = 'res.users'

    helpdesk_team_id = fields.Many2one(
        string='Team',
        comodel_name='helpdesk.team'
    )
    ticket_ids = fields.Many2many(
        string='Users',
        comodel_name='helpdesk.ticket',
        relation='helpdesk_ticket_user_rel',
        column1='user_id',
        column2='ticket_id',
    )
    tickets_count = fields.Integer(
        string='Tickets',
        compute='_compute_total_tickets'
    )

    def _compute_total_tickets(self):
        for record in self:
            record.tickets_count = len(self.env['helpdesk.ticket'].search([('user_ids', 'in', record.id)]))

    def action_show_tickets(self):
        self.ensure_one()
        return {
            'name': _('Record Tickets'),
            'view_mode': 'tree,form',
            'res_model': 'helpdesk.ticket',
            'type': 'ir.actions.act_window',
            'context': {'create': False, 'delete': False},
            'domain': [('id', 'in', self.ticket_ids.ids)],
            'target': 'current',
        }


