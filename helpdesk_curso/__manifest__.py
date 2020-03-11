# -*- coding: utf-8 -*-
# Copyright 2015-2017 See manifest
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

{
    'name': "Helpdesk Curso",
    'version': '13.0.0.0.1',
    'category': 'Generic Modules/Accounting',
    'summary': "Personalizaciones Cliente",
    'author': "Carlos Ramos Hernandez <cramos@puntsistemes.es>",
    'website': '',
    'license': 'AGPL-3',
    'depends': ['sale'],
    'data': [
        'security/helpdesk_security.xml',
        'security/ir.model.access.csv',
        'views/sale_order.xml',
        'views/helpdesk_ticket_views.xml',
    ],
    'test': [
    ],
    'installable': True,
    'application': True,
}