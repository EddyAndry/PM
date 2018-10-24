# -*- encoding: utf-8 -*-

import logging

from odoo import models, api

_logger = logging.getLogger(__name__)


class DMSAccessModel(models.AbstractModel):
    _name = 'dcs_dms.access'
    _description = "MuK Access Model"
    _inherit = 'dcs_security.access_groups'

    _field_groups = 'dcs_dms.group_dms_manager'
    _suspend_groups = 'dcs_dms.group_dms_admin'

    # ----------------------------------------------------------
    # Function
    # ----------------------------------------------------------

    @api.multi
    def _eval_access_skip(self, operation):
        res = super(DMSAccessModel, self)._eval_access_skip(operation)
        if self.user_has_groups('dcs_dms.group_dms_admin'):
            return True
        else:
            return res
