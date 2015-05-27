# -*- coding: utf-8 -*-
from openerp import models, fields, api, _
from openerp.exceptions import Warning


class session(models.Model):
    """"""

    _name = 'openacademy.session'
    _description = 'session'

    _states_ = [
        # State machine: untitle
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('done', 'Done'),
        ('cancel', 'Cancel'),
    ]

    name = fields.Char(
        string='Name',
        required=True
        )
    start_date = fields.Date(
        string='Start Date',
        default=fields.Date.today
        )
    duration = fields.Float(
        string='Durtion',
        required=True
        )
    seats = fields.Integer(
        string='Number of Seats',
        required=True,
        compute='_taken_seats'
        )
    instructor_id = fields.Many2one(
        'res.partner',
        string='Instructor',
        domain=['|',('instructor', '=', True), ('category_id.name', 'ilike', "Teacher")]
        )
    active = fields.Boolean(
        string='Active',
        default=True
        )
    state = fields.Selection(
        _states_,
        'State',
        default='draft',
        )
    partner_ids = fields.Many2many(
        'res.partner',
        'openacademy_partner_ids_session_ids_rel',
        'session_id',
        'partner_id',
        string='Partners'
        )
    course_id = fields.Many2one(
        'openacademy.course',
        ondelete='cascade',
        string='Course',
        required=True
        )

    _constraints = [
    ]

    @api.one
    def _taken_seats(self):
        """"""
        raise NotImplementedError

    @api.multi
    def action_cancel_draft(self):
        # go from canceled state to draft state
        self.write({'state': 'draft'})
        self.delete_workflow()
        self.create_workflow()
        return True

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
