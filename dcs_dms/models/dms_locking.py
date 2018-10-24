# -*- encoding: utf-8 -*-

import logging

from odoo import models, api

_logger = logging.getLogger(__name__)

class DMSLockingModel(models.AbstractModel):
    
    _name = 'dcs_dms.locking'
    _description = 'MuK Document Locking Model'
    _inherit = ['dcs_dms.model', 'dcs_security.locking']

    #----------------------------------------------------------
    # Locking
    #----------------------------------------------------------

    @api.multi
    def lock(self, user=None, operation=None, *largs, **kwargs):
        res = super(DMSLockingModel, self).lock(user, operation, *largs, **kwargs)
        if "refresh" in kwargs and kwargs["refresh"]:
            self.refresh_views(model=self._name, ids=self.ids)
        return res
    
    @api.multi
    def unlock(self, *largs, **kwargs):
        res = super(DMSLockingModel, self).unlock(*largs, **kwargs)
        if "refresh" in kwargs and kwargs["refresh"]:
            self.refresh_views(model=self._name, ids=self.ids)
        return res
    
    @api.model
    def unlock_operation(self, operation, *largs, **kwargs):
        res = super(DMSLockingModel, self).unlock_operation(operation, *largs, **kwargs)
        if "refresh" in kwargs and kwargs["refresh"]:
            for tuple in res:
                self.refresh_views(model=tuple[0], ids=tuple[1])
        return res
    
    @api.multi
    def user_lock(self, *largs, **kwargs):
        res = super(DMSLockingModel, self).user_lock(*largs, **kwargs)
        self.refresh_views()
        return res
    
    @api.multi
    def user_unlock(self, *largs, **kwargs):
        res = super(DMSLockingModel, self).user_unlock(*largs, **kwargs)
        self.refresh_views()
        return res