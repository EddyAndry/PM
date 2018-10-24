# -*- encoding: utf-8 -*-

import logging
import unittest

from odoo.tests import common

_logger = logging.getLogger(__name__)

class UtilsTestCase(common.HttpCase):
    
    at_install = False
    post_install = True
    
    def setUp(self):
        super(UtilsTestCase, self).setUp()

    def tearDown(self):
        super(UtilsTestCase, self).tearDown()
    
    @unittest.skip("PhantomJS")
    def test_common(self):
        self.phantom_js('/web/tests?filter=utils%20>%20common', "", "", login='admin', timeout=360)
        
    @unittest.skip("PhantomJS")
    def test_jquery(self):
        self.phantom_js('/web/tests?filter=utils%20>%20jquery', "", "", login='admin', timeout=360)
    
    @unittest.skip("PhantomJS")
    def test_mimetype(self):
        self.phantom_js('/web/tests?filter=utils%20>%20mimetype', "", "", login='admin', timeout=360)
        