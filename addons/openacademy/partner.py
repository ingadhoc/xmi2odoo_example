# -*- coding: utf-8 -*-
from openerp import models, fields, api, _
from openerp.exceptions import Warning


class partner(models.Model):
    """"""

    _name = 'res.partner'
    _inherits = {}
    _inherit = ['res.partner']

    instructor = fields.Boolean(
        string='Instructor'
        )
    session_ids = fields.Many2many(
        'openacademy.session',
        'openacademy_attendee_ids_session_ids_rel',
        'partner_id',
        'session_id',
        string='Attended Sessions',
        readonly=True
        )

    _constraints = [
    ]

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
