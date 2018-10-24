# -*- encoding: utf-8 -*-

from odoo import api, fields, models

class ResConfigSettings(models.TransientModel):
    
    _inherit = 'res.config.settings'
    
    module_dcs_dms_access = fields.Boolean(
        string="Access Control",
        help="Allows the creation of groups to define access rights.")
    
    module_dcs_dms_widget = fields.Boolean(
        string="Binary Widget Support",
        help="Allows the user to use DMS documents as input for any binary field.")
    
    module_dcs_archive = fields.Boolean(
        string="Download Directories",
        help="Allows to download directories as a archive file.")
    
    module_dcs_dms_thumbnails = fields.Boolean(
        string="Automatic Thumbnails",
        help="Allows the creation of thumbnails for files.")
    
    module_dcs_dms_export = fields.Boolean(
        string="Export Files",
        help="Allows the conversion of existing files.")
    
    module_dcs_dms_attachment = fields.Boolean(
        string="Attachment Storage Location",
        help="Allows attachments to be stored inside of MuK Documents.")

    module_dcs_dms_attachment_rules = fields.Boolean(
        string="Attachment Storage Rules",
        help="Allows attachments to be automatically placed in the right directory.")
    
    module_dcs_dms_attachment_automation = fields.Boolean(
        string="Attachment Rule Automation",
        help="Allows you to create rule templates to create attachment rules.")
    
    module_dcs_dms_attachment_wizard = fields.Boolean(
        string="Attachment Wizard",
        help="Allows documents to be used as attachments.")
    
    module_dcs_dms_finder = fields.Boolean(
        string="Finder",
        help="Enables the Document Finder.")
    
    module_dcs_dms_file = fields.Boolean(
        string="File Store",
        help="Enables a new save option to store files into a file store.")
    
    module_dcs_dms_lobject = fields.Boolean(
        string="Large Objects ",
        help="Enables a new save option to store files into large objects.")
    
    max_upload_size = fields.Integer(
        string="Size",
        help="Defines the maximum upload size in MB. Default (25MB)")
    
    forbidden_extensions = fields.Char(
        string="Extensions",
        help="Defines a list of forbidden file extensions. (Example: '.exe,.msi')")
    
    @api.multi
    def set_values(self):
        res = super(ResConfigSettings, self).set_values()
        param = self.env['ir.config_parameter'].sudo()
        param.set_param('dcs_dms.max_upload_size', self.max_upload_size)
        param.set_param('dcs_dms.forbidden_extensions', self.forbidden_extensions)
        return res

    @api.model
    def get_values(self):
        res = super(ResConfigSettings, self).get_values()
        params = self.env['ir.config_parameter'].sudo()
        res.update(
            max_upload_size=int(params.get_param('dcs_dms.max_upload_size', default=25)),
            forbidden_extensions=params.get_param('dcs_dms.forbidden_extensions', default=""),
        )
        return res
