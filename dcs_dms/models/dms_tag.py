# -*- encoding: utf-8 -*-

import logging

from odoo import models, api, fields

_logger = logging.getLogger(__name__)

class Tag(models.Model):
    
    _name = 'dcs_dms.tag'
    _description = "MuK Document Tag"
    
    #----------------------------------------------------------
    # Database
    #----------------------------------------------------------
    
    name = fields.Char(
        string='Name', 
        required=True, 
        translate=True)
    
    color = fields.Integer(
        string='Color Index', 
        default=10)

    _sql_constraints = [
        ('name_uniq', 'unique (name)', "Tag name already exists!"),
    ]