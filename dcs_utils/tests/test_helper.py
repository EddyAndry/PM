# -*- encoding: utf-8 -*-

import os
import logging

from odoo.tests import common

from odoo.addons.dcs_utils.tools import helper

_path = os.path.dirname(os.path.dirname(__file__))
_logger = logging.getLogger(__name__)

class HelperTestCase(common.HttpCase):
    
    def setUp(self):
        super(HelperTestCase, self).setUp()

    def tearDown(self):
        super(HelperTestCase, self).tearDown()

    def test_slugify(self):
        self.assertTrue(helper.slugify("Test"))