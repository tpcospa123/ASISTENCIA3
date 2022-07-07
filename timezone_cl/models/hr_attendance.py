# -*- coding: utf-8 -*-

import pytz
from odoo import models, fields, api


class HrAttendance(models.Model):
    _inherit = 'hr.attendance'

    check_in_cl = fields.Datetime(compute='_compute_get_date_timezone', )
    check_out_cl = fields.Datetime(compute='_compute_get_date_timezone', )

    @api.depends('check_in', 'check_out')
    def _compute_get_date_timezone(self):
        for rec in self:
            rec.check_in_cl = self.change_timezone_date_cl(rec.check_in)
            rec.check_out_cl = self.change_timezone_date_cl(rec.check_out)

    @api.model
    def change_timezone_date_cl(self, date):
        if not date:
            return False

        timezone = pytz.timezone(self._context.get('tz') or self.env.user.tz or 'UTC')
        print(timezone, date)
        return date.astimezone(timezone).replace(tzinfo=None)
