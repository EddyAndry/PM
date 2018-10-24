# -*- encoding: utf-8 -*-

import logging

from odoo import models, api, fields

_logger = logging.getLogger(__name__)
        
class DatabaseDataModel(models.Model):
    
    _name = 'dcs_dms.data_database'
    _description = 'Database Data Model'
    _inherit = 'dcs_dms.data'
    
    #----------------------------------------------------------
    # Database
    #----------------------------------------------------------
    
    data = fields.Binary(
        string="Content")
    
    #----------------------------------------------------------
    # Abstract Implementation
    #----------------------------------------------------------
    
    @api.multi
    def type(self):
        return "database"
    
    @api.multi
    def content(self):
        self.ensure_one()
        return self.data
    
    @api.multi
    def update(self, values):
        if 'content' in values:
            self.write({'data': values['content']})