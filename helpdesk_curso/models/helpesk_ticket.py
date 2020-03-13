# -*- coding: utf-8 -*-
# Copyright 2020 See manifest
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from odoo import models, fields, api, _
from odoo.exceptions import Warning


class HelpdeskTicket(models.Model):
    _name = 'helpdesk.ticket'
    _description = 'Ticket'
    _inherit = ['mail.thread.cc', 'mail.activity.mixin']

    name = fields.Char(
        string='Name',
        required=True
    )
    partner_id = fields.Many2one(
        string='Partner',
        comodel_name='res.partner',
        required=True
    )
    description = fields.Text(
        string='Description'
    )
    date_deadline = fields.Date(
        string='Date Limit'
    )
    team_id = fields.Many2one(
        string='Team',
        comodel_name='helpdesk.team'
    )
    ticket_stage_id = fields.Many2one(
        string='Stage',
        comodel_name='helpdesk.ticket.stage',
        index=True,
        required=True,
        tracking=True,
        default=1
    )
    user_ids = fields.Many2many(
        string='Users',
        comodel_name='res.users',
        relation='helpdesk_ticket_user_rel',
        column1='ticket_id',
        column2='user_id',
        tracking=True
    )
    tickets_qty = fields.Integer(
        string='Ticket Qty',
        compute="_compute_tickets_qty"
    )
    displayed_image_id = fields.Many2one(
        comodel_name='ir.attachment',
        domain="[('res_model', '=', 'res.partner'), ('res_id', '=', partner_id), ('mimetype', 'ilike', 'image')]",
        string='Cover Image'
    )

    @api.depends('user_ids')
    def _compute_tickets_qty(self):
        for record in self:
            ticket_ids = record.search_count([('user_ids', 'in', record.user_ids.ids)])
            self.tickets_qty = ticket_ids

    @api.onchange('name', 'date_deadline')
    def _onchange_description(self):
        self.description = '%s - %s' % (self.name or 'Ticket', self.date_deadline or 'Sin fecha programada')

    def btn_auto_assign(self):
        self.ensure_one()  # NOS SEGURAMOS QUE SOLO SE EJECUTE CUANDO SELF TENGA UN REGISTRO
        if self.env.user.id not in self.user_ids.ids:
            self.user_ids = [4, self.env.user.id]  # Añadimos un valor a un campo Many2many
        else:
            raise Warning(_('This user is just assigned from task.'))

