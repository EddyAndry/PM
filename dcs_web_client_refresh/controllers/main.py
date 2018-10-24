# -*- encoding: utf-8 -*-

import logging

from odoo import http
from odoo.http import request

_logger = logging.getLogger(__name__)

class RefreshController(http.Controller):

    @http.route('/config/dcs_web_client_refresh.refresh_delay', type='json', auth="user")
    def refresh_delay(self, **kw):
        params = request.env['ir.config_parameter'].sudo()
        return {
            'refresh_delay': int(params.get_param("dcs_web_client_refresh.refresh_delay", default=1000))
        }