# -*- encoding: utf-8 -*-

import logging

from odoo import models, api, fields

_logger = logging.getLogger(__name__)

class Lock(models.Model):
    
    _name = 'dcs_security.lock'
    _description = "Lock"

    name = fields.Char(
        compute='_compute_lock_ref_data',
        string="Name",
        store=True)

    locked_by = fields.Char(
        string="Locked by",
        readonly=True,
        required=True)
    
    locked_by_ref = fields.Many2one(
        comodel_name='res.users',
        string="Locked by")

    lock_ref = fields.Reference(
        selection=[],
        string="Reference",
        required=True)
    
    lock_ref_model = fields.Char(
        compute='_compute_lock_ref_data',
        string="Reference Model",
        store=True)
    
    lock_ref_id = fields.Char(
        compute='_compute_lock_ref_data',
        string="Reference ID",
        store=True)
    
    token = fields.Char(
        string="Token")
    
    operation = fields.Char(
        string="Operation")
    
    @api.depends('lock_ref')
    def _compute_lock_ref_data(self):
        for record in self:
            record.update({
                'name': "Lock for " + str(record.lock_ref.display_name),
                'lock_ref_model': record.lock_ref._name,
                'lock_ref_id': record.lock_ref.id})
            