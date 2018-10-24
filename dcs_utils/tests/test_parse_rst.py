# -*- encoding: utf-8 -*-

import os
import logging

from odoo.tests import common

from odoo.addons.dcs_utils.tools import parse_rst

_path = os.path.dirname(os.path.dirname(__file__))
_logger = logging.getLogger(__name__)

class ParseReStructuredTextTestCase(common.HttpCase):
    
    def setUp(self):
        super(ParseReStructuredTextTestCase, self).setUp()

    def tearDown(self):
        super(ParseReStructuredTextTestCase, self).tearDown()
        
    def test_rst2html(self):
        self.assertTrue(parse_rst.rst2html("Test"))