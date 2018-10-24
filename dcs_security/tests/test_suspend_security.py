# -*- encoding: utf-8 -*-

import os
import base64
import logging

from odoo import exceptions
from odoo.tests import common

_path = os.path.dirname(os.path.dirname(__file__))
_logger = logging.getLogger(__name__)

class SuspendSecurityTestCase(common.TransactionCase):
    
    at_install = False
    post_install = True
    
    def setUp(self):
        super(SuspendSecurityTestCase, self).setUp()
        
    def tearDown(self):
        super(SuspendSecurityTestCase, self).tearDown()
    
    def test_suspend_security(self):
        user_id = self.env.ref('base.user_demo').id
        with self.assertRaises(exceptions.AccessError):
            self.env.ref('base.user_root').sudo(user_id).name = 'test'
        self.env.ref('base.user_root').sudo(user_id).suspend_security().name = 'test'
        self.assertEqual(self.env.ref('base.user_root').name, 'test')
        self.assertEqual(self.env.ref('base.user_root').write_uid.id, user_id)
        
    def test_normalize(self):
        self.env['res.users'].browse(self.env['res.users'].suspend_security().env.uid)