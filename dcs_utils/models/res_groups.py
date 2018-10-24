# -*- encoding: utf-8 -*-

import logging

from collections import defaultdict

from odoo import api, fields, models
from odoo import tools, _
from odoo.exceptions import ValidationError

_logger = logging.getLogger(__name__)

class ResGroups(models.Model):
    
    _inherit = "res.groups"

    #----------------------------------------------------------
    # Create, Update, Delete
    #----------------------------------------------------------

    @api.multi
    def write(self, vals):
        model_recs = defaultdict(set)
        model_names = self.pool.descendants(['dcs_utils.groups'], '_inherit', '_inherits')
        if any(field in vals for field in ['users']):
            for model_name in model_names:
                model = self.env[model_name].sudo()
                if not model._abstract:
                    model_recs[model_name] = model.search([['groups', 'in', self.mapped('id')]])
        result = super(ResGroups, self).write(vals)
        if any(field in vals for field in ['users']):
            for model_name in model_names:
                model = self.env[model_name].sudo()
                if not model._abstract:
                    model_recs[model_name] = model_recs[model_name] | model.search([['groups', 'in', self.mapped('id')]])
            for tuple in model_recs.items():
                tuple[1].trigger_computation(['users'])
        return result
    
    @api.multi
    def unlink(self):
        model_recs = defaultdict(set)
        model_names = self.pool.descendants(['dcs_utils.groups'], '_inherit', '_inherits')
        for model_name in model_names:
            model = self.env[model_name].sudo()
            if not model._abstract:
                model_recs[model_name] = model.search([['groups', 'in', self.mapped('id')]])
        result = super(ResGroups, self).unlink(vals)
        for tuple in model_recs.items():
            tuple[1].trigger_computation(['users'])
        return result