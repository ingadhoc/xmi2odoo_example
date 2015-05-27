# -*- coding: utf-8 -*-
from openerp import models, fields, api, _
from openerp.exceptions import Warning


class course(models.Model):
    """"""

    _name = 'openacademy.course'
    _description = 'course'
    _inherits = {}
    _inherit = ['mail.thread','ir.needaction_mixin']

    _track = {
    }

    name = fields.Char(
        string='Name',
        required=True
        )
    description = fields.Text(
        string='Description'
        )
    responsible_id = fields.Many2one(
        'res.users',
        string='Responsible'
        )
    session_ids = fields.One2many(
        'openacademy.session',
        'course_id',
        string='Sessions'
        )

    _constraints = [
    ]

    @api.one
    def _taken_seats(self):
        """"""
        parent = super(course,self)
        result = parent._taken_seats() if hasattr(parent, '_taken_seats') else False
        return result

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
