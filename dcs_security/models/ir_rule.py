# -*- encoding: utf-8 -*-
import logging

from odoo import api, fields, models
from odoo import tools, _
from odoo.exceptions import ValidationError

from odoo.addons.dcs_security.tools import helper

_logger = logging.getLogger(__name__)

class ExtendedIrRule(models.Model):
    
    _inherit = 'ir.rule'
    
    @api.model
    @tools.ormcache('self._uid', 'model_name', 'mode')
    def _compute_domain(self, model_name, mode="read"):
        if isinstance(self.env.uid, helper.NoSecurityUid):
            return None
        return super(ExtendedIrRule, self)._compute_domain(model_name, mode=mode)