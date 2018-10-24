# -*- encoding: utf-8 -*-

import logging
import datetime

from odoo.tests import common
from odoo.tools.misc import DEFAULT_SERVER_DATETIME_FORMAT

_logger = logging.getLogger(__name__)

class AutoVacuumTestCase(common.TransactionCase):
    
    at_install = False
    post_install = True
    
    def _setUpData(self):
        model_logs = self.env['ir.logging']
        time = datetime.datetime.utcnow() - datetime.timedelta(days=60)
        for index in range(0, 3):
            model_logs.create({
                'create_date': time.strftime(DEFAULT_SERVER_DATETIME_FORMAT),
                'create_uid': self.env.user.id,
                'name': "Test %s" % index,
                'type': 'server',
                'dbname': self.env.cr.dbname,
                'level': "INFO",
                'message': "TEST",
                'path': "PATH",
                'func': "TEST",
                'line': 1})

    def _setUpRules(self):
        model_rule = self.env['dcs_autovacuum.rules']
        model_model = self.env['ir.model']
        model_fields = self.env['ir.model.fields']
        model_logs = model_model.search([('model', '=', 'ir.logging')], limit=1)
        time_field_domain = [
            ('model_id', '=', model_logs.id),
            ('ttype', '=', 'datetime'),
            ('name', '=', 'create_date')]
        time_field_logs = model_fields.search(time_field_domain, limit=1)
        model_rule.create({
            'name': "Delete Logs after 1 Minute",
            'state': 'time',
            'model': model_logs.id,
            'time_field': time_field_logs.id,
            'time_type': 'minutes',
            'time': 1})
        model_rule.create({
            'name': "Delete Logs Count > 1",
            'state': 'size',
            'model': model_logs.id,
            'size': 1,
            'size_order': "id desc",
            'size_type': 'fixed'})
        model_rule.create({
            'name': "Delete Logs with Domain",
            'state': 'domain',
            'model': model_logs.id,
            'domain': "[]"})
    
    def setUp(self):
        super(AutoVacuumTestCase, self).setUp()
        self._setUpData()
        self._setUpRules()
        
    def tearDown(self):
        super(AutoVacuumTestCase, self).tearDown()
    
    def test_autovacuum(self):
        self.env['ir.cron'].search([('model_id', '=', 'ir.autovacuum')]).ir_actions_server_id.run()