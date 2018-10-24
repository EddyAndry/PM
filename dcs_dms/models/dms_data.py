# -*- encoding: utf-8 -*-

import logging

from odoo import models, api

_logger = logging.getLogger(__name__)

class DataModel(models.AbstractModel):
    
    _name = 'dcs_dms.data'
    _description = 'Base Data Model'
    
    @api.model
    def type(self):
        """Returns the data type."""
    
    @api.multi
    def content(self):
        """Returns the data object."""
    
    @api.multi
    def update(self, values):
        """Updated the data object."""