

import os
import logging
import unittest
import collections

from odoo.addons.dcs_dms.tests import dms_case

_path = os.path.dirname(os.path.dirname(__file__))
_logger = logging.getLogger(__name__)

_compare = lambda x, y: collections.Counter(x) == collections.Counter(y)

class SettingsTestCase(dms_case.DMSTestCase):
    
    @unittest.skipIf(os.environ.get('TRAVIS', False), "Skipped for Travis CI")
    def test_top_directories(self):
        settings = self.browse_ref("dcs_dms.settings_demo")
        directories = self.directory.sudo().search([('is_top_directory', '=', True)]) 
        self.assertTrue(_compare(directories, settings.sudo().top_directories))
        
    @unittest.skipIf(os.environ.get('TRAVIS', False), "Skipped for Travis CI")
    def test_top_files(self):
        settings = self.browse_ref("dcs_dms.settings_demo")
        files = self.file.sudo().search([('is_top_file', '=', True)]) 
        self.assertTrue(_compare(files, settings.sudo().top_files))
