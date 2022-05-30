# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    bank_last_update = fields.Datetime(string='Última Revisión', default=fields.Datetime.now)
    bank_last_update_by = fields.Many2one('res.users', string='Revisado por', default=lambda self: self.env.user.id)
