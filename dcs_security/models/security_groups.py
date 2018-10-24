# -*- encoding: utf-8 -*-

from odoo import models, fields, api

class AccessGroups(models.Model):
    
    _name = 'dcs_security.groups'
    _description = "Access Groups"
    _inherit = 'dcs_utils.groups'
    
    #----------------------------------------------------------
    # Database
    #----------------------------------------------------------
    
    perm_read = fields.Boolean(
        string='Read Access')
    
    perm_create = fields.Boolean(
        string='Create Access')
    
    perm_write = fields.Boolean(
        string='Write Access')
    
    perm_unlink = fields.Boolean(
        string='Unlink Access')
 