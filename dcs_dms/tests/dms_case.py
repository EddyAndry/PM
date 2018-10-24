# -*- encoding: utf-8 -*-

import os
import base64
import logging

from odoo import SUPERUSER_ID
from odoo.tests import common

_path = os.path.dirname(os.path.dirname(__file__))
_logger = logging.getLogger(__name__)

class DMSTestCase(common.TransactionCase):
    
    at_install = False
    post_install = True
    
    def setUp(self):
        super(DMSTestCase, self).setUp()
        self.adminuser = SUPERUSER_ID
        self.demouser = self.browse_ref("base.user_demo").id
        self.settings = self.env['dcs_dms.settings']
        self.directory = self.env['dcs_dms.directory']
        self.file = self.env['dcs_dms.file']
        
    def tearDown(self):
        super(DMSTestCase, self).tearDown()
        
    def file_base64(self):
        return base64.b64encode(b"\xff data")