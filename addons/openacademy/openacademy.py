# -*- coding: utf-8 -*-
from openerp import models, fields, api, _
from openerp.exceptions import Warning


class openacademy(models.Model):
    """"""

    _name = 'openacademy.openacademy'
    _description = 'openacademy'

    name = fields.Char(
        string='Name'
        )

    _constraints = [
    ]

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
