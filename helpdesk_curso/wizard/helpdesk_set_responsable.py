# -*- coding: utf-8 -*-
# Copyright 2015-2017 See manifest
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from odoo import models, fields, api, _
from odoo.exceptions import Warning


class HelpdeskSetResponsable(models.TransientModel):
    _name = "helpdesk.set.responsable"

    def _default_ticket_count(self):
        return len(self.env['helpdesk.ticket'].search([('user_ids', 'in', self.env.user.id)]))

    @api.model
    def default_get(self, fields):
        res = super(HelpdeskSetResponsable, self).default_get(fields)
        user_id = self.env.uid
        ticket_ids = len(self.env['helpdesk.ticket'].search([('user_ids', 'in', self.env.user.id)]))
        res['user_ticket_count'] = ticket_ids
        return res

    user_ticket_count = fields.Integer(
        string='Cont tickets',
        #default=_default_ticket_count,
        readonly=True
    )

    def set_responsable(self):
        self.ensure_one()
        # self.ticket = self.env['helpdesk.ticket'].search([('id', '=', self._context.get('active_id'))])
        self.ticket = self.env['helpdesk.ticket'].browse(self.env.context.get('active_id'))

        if self.env.user.id not in self.ticket.user_ids.ids:
            self.ticket.user_ids = [4, self.env.user.id]  # Añadimos un valor a un campo Many2many
        else:
            raise Warning(_('This user is just assigned from task.'))
        # ticket.responsable_id = self.env.user
