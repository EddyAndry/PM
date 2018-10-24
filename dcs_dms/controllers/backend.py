# -*- encoding: utf-8 -*-

import logging

from odoo import _, http
from odoo.http import request

_logger = logging.getLogger(__name__)

class BackendController(http.Controller):
    
    @http.route('/config/dcs_dms.max_upload_size', type='json', auth="user")
    def max_upload_size(self, **kw):
        params = request.env['ir.config_parameter'].sudo()
        return {
            'max_upload_size': int(params.get_param("dcs_dms.max_upload_size", default=25))
        }

    @http.route('/config/dcs_dms.forbidden_extensions', type='json', auth="user")
    def forbidden_extensions(self, **kw):
        params = request.env['ir.config_parameter'].sudo()
        return {
            'forbidden_extensions': params.get_param("dcs_dms.forbidden_extensions", default="")
        }
    
    @http.route('/tree/create/directory', type='json', auth="user")
    def create_directory(self, parent_directory, name=None, context=None, **kw):
        parent = request.env['dcs_dms.directory'].sudo().browse(parent_directory)
        uname = parent.unique_name(name or _("New Directory"), parent.child_directories.mapped('name'))
        directory = request.env['dcs_dms.directory'].with_context(context or request.env.context).create({
            'name': uname,
            'parent_directory': parent_directory})
        return {
            'id': "directory_%s" % directory.id,
            'text': directory.name,
            'icon': "fa fa-folder-o",
            'type': "directory",
            'data': {
                'odoo_id': directory.id,
                'odoo_model': "dcs_dms.directory",
                'odoo_record': False,
                'name': directory.name,
                'perm_read': directory.permission_read,
                'perm_create': directory.permission_create,
                'perm_write': directory.permission_write,
                'perm_unlink': directory.permission_unlink,
                'directories': directory.count_directories,
                'files': directory.count_files,
                'parent': "directory_%s" % parent_directory,
            },
            'children': False,
        }    