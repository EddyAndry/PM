# -*- encoding: utf-8 -*-

from odoo import api, fields, models

class ResConfigSettings(models.TransientModel):

    _inherit = 'res.config.settings'

    refresh_delay = fields.Integer(
        string="Delay",
        help="""Prevents multiple executions of refresh in a certain timeframe to avoid the view from being
            reloaded too often. For example, a delay of 1000 (ms) would mean that the view cannot be
            reloaded more than once a second.""")
    
    @api.multi 
    def set_values(self):
        res = super(ResConfigSettings, self).set_values()
        param = self.env['ir.config_parameter'].sudo()
        param.set_param("dcs_web_client_refresh.refresh_delay", self.refresh_delay)
        return res

    @api.model
    def get_values(self):
        res = super(ResConfigSettings, self).get_values()
        params = self.env['ir.config_parameter'].sudo()
        res.update(refresh_delay=int(params.get_param("dcs_web_client_refresh.refresh_delay", default=1000)))
        return res
