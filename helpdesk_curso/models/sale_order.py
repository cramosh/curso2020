# -*- coding: utf-8 -*-
# Copyright 2020 See manifest
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from odoo import models, fields, api, exceptions, _

class SaleOrder(models.Model):

    _inherit = 'sale.order'

    pnt_delivery_date = fields.Date(
        string='Delivery Date'
    )
