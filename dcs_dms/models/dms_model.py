# -*- encoding: utf-8 -*-

import os
import shutil
import logging
import tempfile

from odoo import models, api

from odoo.addons.dcs_utils.tools import helper
from odoo.addons.dcs_utils.tools import utils_os

_logger = logging.getLogger(__name__)

class DMSBaseModel(models.AbstractModel):
    
    _name = 'dcs_dms.model'
    _description = 'MuK Document Base Model'
    _inherit = 'dcs_utils.model'

    #----------------------------------------------------------
    # Function
    #----------------------------------------------------------
    
    @api.multi
    def notify_change(self, values, *largs, **kwargs):
        super(DMSBaseModel, self).notify_change(values, *largs, **kwargs)
        if "refresh" in kwargs and kwargs["refresh"]:
            self.refresh_views()
    
    @api.multi
    def trigger_computation(self, fields, *largs, **kwargs):
        super(DMSBaseModel, self).trigger_computation(fields, *largs, **kwargs)
        if "refresh" in kwargs and kwargs["refresh"]:
            self.refresh_views()
    
        
    @api.model
    def check_name(self, name):
        tmp_dir = tempfile.mkdtemp()
        try:
            open(os.path.join(tmp_dir, name), 'a').close()
        except IOError:
            return False
        finally:
            shutil.rmtree(tmp_dir)
        return True
    
    @api.model
    def unique_name(self, name, names, escape_suffix=False):
        return utils_os.unique_name(name, names, escape_suffix)
    
    @api.multi
    def refresh_views(self, model=None, ids=None, user=None, create=False):
        if self.exists() or ids:
            record = next(iter(self)) if len(self) > 1 else self
            self.env["bus.bus"].sendone("refresh", {
                "create": create if ids else record.exists() and record.create_date == record.write_date or False,
                "model": model or self._name,
                "uid": user and user.id or False if ids else self.env.user.id,
                "ids": ids or (record | self).mapped("id")})