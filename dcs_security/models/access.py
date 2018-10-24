# -*- encoding: utf-8 -*-

import logging

from odoo import _
from odoo import models, api, fields
from odoo.exceptions import AccessError

_logger = logging.getLogger(__name__)

class BaseModelAccess(models.AbstractModel):
    
    _name = 'dcs_security.access'
    _description = "MuK Access Model"
    _inherit = 'dcs_utils.model'
    
    #----------------------------------------------------------
    # Database
    #----------------------------------------------------------
            
    permission_read = fields.Boolean(
        compute='_compute_permissions',
        search='_search_permission_read',
        string="Read Access")
    
    permission_create = fields.Boolean(
        compute='_compute_permissions',
        search='_search_permission_create',
        string="Create Access")
    
    permission_write = fields.Boolean(
        compute='_compute_permissions',
        search='_search_permission_write',
        string="Write Access")
    
    permission_unlink = fields.Boolean(
        compute='_compute_permissions', 
        search='_search_permission_unlink',
        string="Delete Access")
        
    #----------------------------------------------------------
    # Function
    #----------------------------------------------------------
    
    @api.model
    def check_access_rights(self, operation, raise_exception=True):
        return super(BaseModelAccess, self).check_access_rights(operation, raise_exception)
    
    @api.multi
    def check_access_rule(self, operation):
        return super(BaseModelAccess, self).check_access_rule(operation)
    
    @api.model
    def _apply_ir_rules(self, query, mode='read'):
        return super(BaseModelAccess, self)._apply_ir_rules(query, mode)
    
    @api.model
    def check_field_access_rights(self, operation, fields):
        return super(BaseModelAccess, self).check_field_access_rights(operation, fields)
    
    @api.multi
    def check_access(self, operation, raise_exception=False):
        try:
            access_right = self.check_access_rights(operation, raise_exception)
            access_rule = self.check_access_rule(operation) == None
            access = access_right and access_rule
            if not access and raise_exception:
                raise AccessError(_("This operation is forbidden!"))
            return access
        except AccessError:
            if raise_exception:
                raise AccessError(_("This operation is forbidden!"))
            return False

    #----------------------------------------------------------
    # Search
    #----------------------------------------------------------
    
    @api.model
    def _search_permission_read(self, operator, operand):
        records = self.search([]).filtered(lambda r: r.check_access('read') == True)
        if operator == '=' and operand:
            return [('id', 'in', records.mapped('id'))]
        return [('id', 'not in', records.mapped('id'))]
    
    @api.model
    def _search_permission_create(self, operator, operand):
        records = self.search([]).filtered(lambda r: r.check_access('create') == True)
        if operator == '=' and operand:
            return [('id', 'in', records.mapped('id'))]
        return [('id', 'not in', records.mapped('id'))]
    
    @api.model
    def _search_permission_write(self, operator, operand):
        records = self.search([]).filtered(lambda r: r.check_access('write') == True)
        if operator == '=' and operand:
            return [('id', 'in', records.mapped('id'))]
        return [('id', 'not in', records.mapped('id'))]
    
    @api.model
    def _search_permission_unlink(self, operator, operand):
        records = self.search([]).filtered(lambda r: r.check_access('unlink') == True)
        if operator == '=' and operand:
            return [('id', 'in', records.mapped('id'))]
        return [('id', 'not in', records.mapped('id'))]

    #----------------------------------------------------------
    # Read, View 
    #----------------------------------------------------------
    
    @api.multi
    def _compute_permissions(self):
        for record in self:
            record.update({
                'permission_read': record.check_access('read'),
                'permission_create': record.check_access('create'),
                'permission_write': record.check_access('write'),
                'permission_unlink': record.check_access('unlink'),
            })