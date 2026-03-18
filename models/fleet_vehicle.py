from odoo import fields, models
from odoo.exceptions import UserError

import datetime, pytz, json, logging, warnings
_logger = logging.getLogger(__name__)


class vehicle(models.Model):
    _inherit = "fleet.vehicle"

    customer_id = fields.Many2one('res.partner', string='Customer')





