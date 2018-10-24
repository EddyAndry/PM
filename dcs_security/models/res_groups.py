# -*- encoding: utf-8 -*-

import logging

from odoo import api, fields, models
from odoo import tools, _
from odoo.exceptions import ValidationError

_logger = logging.getLogger(__name__)

class AccessGroups(models.Model):
    
    _inherit = "res.groups"

    #----------------------------------------------------------
    # Database
    #----------------------------------------------------------
    
    security_groups = fields.Many2many(
        comodel_name='dcs_security.groups',
        relation='dcs_security_groups_groups_rel',
        column1='rid',
        column2='gid',
        string='Groups')