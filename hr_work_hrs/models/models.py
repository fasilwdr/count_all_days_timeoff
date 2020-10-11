# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.addons.resource.models.resource import float_to_time, HOURS_PER_DAY


class HolidaysRequest(models.Model):
    _inherit = "hr.leave"

    def _get_number_of_days(self, date_from, date_to, employee_id):
        days = (date_to - date_from).days + 1
        return {'days': days, 'hours': HOURS_PER_DAY * days}
