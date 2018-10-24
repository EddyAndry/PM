# -*- encoding: utf-8 -*-

from odoo import fields, models

class ResConfigSettings(models.TransientModel):

    _inherit = 'res.config.settings'

    module_dcs_web_client_refresh = fields.Boolean(
        string="Web Refresh",
        help="Define action rules to automatically refresh views.")
    
    module_dcs_web_client_notification = fields.Boolean(
        string="Web Notification",
        help="Send instant messages to users in real time.")
    