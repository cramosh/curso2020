from odoo.test import SavePointCase


class TestHelpdeskTicket(SavePointCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.team_obj = cls.env['helpdesk.team']
        cls.ticket_obj = cls.env['helpdesk.ticket']
        cls.ticket_stage_obj = cls.env['helpdesk.ticket.stage']
        cls.user_obj = cls.env['res.users']

        cls.user_demo = cls.env.ref(
            'base.user_demo')  # dentro de ref añadimos el xml_id que puedo consultar en los metadatos del modelo res.users
        cls.user_admin = cls.env.ref('base.user_admin')

        def test_create_ticket(self):
            date = 'no date'
            ticket_name = "test ticket"
            ticket = self.ticket_obj.create({
                'name': ticket_name,
                'user_ids': "a2s"
            })
            self.assertEqual(ticket.description, 'test ticket - no date')
