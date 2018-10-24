# -*- encoding: utf-8 -*-

import os
import logging
import unittest

from odoo.tests import common

_path = os.path.dirname(os.path.dirname(__file__))
_logger = logging.getLogger(__name__)

class PreviewTestCase(common.HttpCase):
    
    at_install = False
    post_install = True
    
    def setUp(self):
        super(PreviewTestCase, self).setUp()

    def tearDown(self):
        super(PreviewTestCase, self).tearDown()
    
    @unittest.skip("PhantomJS")
    def test_preview(self):
        self.phantom_js("/web?debug=",
                        "odoo.__DEBUG__.services['web_tour.tour'].run('preview')",
                        "odoo.__DEBUG__.services['web_tour.tour'].tours.preview.ready",
                        login="admin")
        