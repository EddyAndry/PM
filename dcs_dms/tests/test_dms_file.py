# -*- encoding: utf-8 -*-

import os
import logging

from odoo.addons.dcs_dms.tests import dms_case

_path = os.path.dirname(os.path.dirname(__file__))
_logger = logging.getLogger(__name__)

class FileTestCase(dms_case.DMSTestCase):
    
    def test_compute_thumbnail(self):
        file = self.browse_ref("dcs_dms.file_14_demo")
        self.assertTrue(file.thumbnail)
        
    def test_create_file(self):
        directory = self.browse_ref("dcs_dms.directory_12_demo")
        file = self.file.create({
            'name': "file.txt",
            'directory': directory.id,
            'content': self.file_base64()})
        self.assertTrue(file.extension == '.txt')
        
    def test_lock_file(self):
        file = self.browse_ref("dcs_dms.file_14_demo")
        file.user_lock()
        self.assertTrue(file.is_locked_by())
        file.user_unlock()
        
    def test_unlink_file(self):
        directory = self.browse_ref("dcs_dms.directory_12_demo")
        file = self.file.create({
            'name': "file.txt",
            'directory': directory.id,
            'content': self.file_base64()})
        file.unlink()
        self.assertFalse(file.exists())