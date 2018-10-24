# -*- encoding: utf-8 -*-

import logging

from odoo import api, fields, models
from odoo import tools, _
from odoo.exceptions import ValidationError

from odoo.addons.base.res import res_users

from odoo.addons.dcs_security.tools import helper

_logger = logging.getLogger(__name__)

class AccessUser(models.Model):
    
    _inherit = 'res.users'

    #----------------------------------------------------------
    # Database
    #----------------------------------------------------------
    
    security_groups = fields.Many2many(
        comodel_name='dcs_security.groups',
        relation='dcs_security_groups_explicit_users_rel',
        column1='uid',
        column2='gid',
        string='Groups',
        readonly=True)

    #----------------------------------------------------------
    # Functions
    #----------------------------------------------------------
    
    @classmethod
    def _browse(cls, ids, env, prefetch=None):
        return super(AccessUser, cls)._browse([
            id if not isinstance(id, helper.NoSecurityUid)
            else super(helper.NoSecurityUid, id).__int__() 
            for id in ids], env, prefetch=prefetch)