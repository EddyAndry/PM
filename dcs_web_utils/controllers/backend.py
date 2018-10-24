# -*- encoding: utf-8 -*-

import logging

from odoo import _, http
from odoo.http import request

_logger = logging.getLogger(__name__)

class BackendController(http.Controller):

    @http.route('/helper/fields/model', type='json', auth="user")
    def get_model(self, id, **kw):
        return {'model_name': request.env['ir.model'].sudo().browse(id).model}
        
        