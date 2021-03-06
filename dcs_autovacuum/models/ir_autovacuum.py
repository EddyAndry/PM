# -*- encoding: utf-8 -*-

import time
import logging
import datetime
import dateutil

from odoo import _
from odoo import models, api
from odoo.tools.safe_eval import safe_eval
from odoo.tools.misc import DEFAULT_SERVER_DATETIME_FORMAT

_logger = logging.getLogger(__name__)

_types = {
    'days': lambda interval: datetime.timedelta(days=interval),
    'years': lambda interval: datetime.timedelta(weeks=interval*52),
    'hours': lambda interval: datetime.timedelta(hours=interval),
    'weeks': lambda interval: datetime.timedelta(weeks=interval),
    'months': lambda interval: datetime.timedelta(days=interval*30),
    'minutes': lambda interval: datetime.timedelta(minutes=interval),
}

class AutoVacuum(models.AbstractModel):
    
    _inherit = 'ir.autovacuum'
    
    @api.model
    def power_on(self, *args, **kwargs):
        res = super(AutoVacuum, self).power_on(*args, **kwargs)
        rules = self.env['dcs_autovacuum.rules'].sudo().search([], order='sequence asc')
        for rule in rules:
            if rule.state in ['time', 'size', 'domain']:
                model = self.env[rule.model.model].sudo()
                records = self.env[rule.model.model]
                if rule.state == 'time':
                    computed_time = datetime.datetime.utcnow() - _types[rule.time_type](rule.time)
                    domain = [(rule.time_field.name, '<', computed_time.strftime(DEFAULT_SERVER_DATETIME_FORMAT))]
                    if rule.protect_starred:
                       for field in rule.model.field_id:
                           if field.name in ['starred', 'favorite', 'is_starred', 'is_favorite']:
                                domain.append((field.name, '=', False))
                    if rule.only_inactive and "active" in rule.model.field_id.mapped("name"):
                        domain.append(('active', '=', False))
                    _logger.info(_("GC domain: %s"), domain)
                    records = model.with_context({'active_test': False}).search(domain)
                elif rule.state == 'size':
                    size = rule.size if rule.size_type == 'fixed' else rule.size_parameter_value
                    count = model.with_context({'active_test': False}).search([], count=True)
                    if count > size:
                        limit = count - size
                        _logger.info(_("GC domain: [] order: %s limit: %s"), rule.size_order, limit)
                        records = model.with_context({'active_test': False}).search([], order=rule.size_order, limit=limit)
                elif rule.state == 'domain':
                    _logger.info(_("GC domain: %s"), rule.domain)
                    domain = safe_eval(rule.domain, rules._get_eval_domain_context())
                    records = model.with_context({'active_test': False}).search(domain)
                if rule.only_attachments:
                    attachments = self.env['ir.attachment'].sudo().search([
                        ('res_model', '=', rule.model.model),
                        ('res_id', 'in', records.mapped('id'))])
                    count = len(attachments)
                    attachments.unlink()
                    _logger.info(_("GC'd %s attachments from %s entries"), count, rule.model.model)
                else:
                    count = len(records)
                    records.unlink()
                    _logger.info(_("GC'd %s %s records"), count, rule.model.model)
            elif rule.state == 'code':
                safe_eval(rule.code.strip(), rules._get_eval_code_context(rule), mode="exec")        
        return res