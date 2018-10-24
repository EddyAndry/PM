# -*- encoding: utf-8 -*-

from odoo import api, fields, models

class ResConfigSettings(models.TransientModel):

    _inherit = 'res.config.settings'

    module_dcs_web_preview_audio = fields.Boolean(
        string="Preview Audio",
        help="Extendes the Preview Dialog to support audio.")
    
    module_dcs_web_preview_csv = fields.Boolean(
        string="Preview CSV",
        help="Extendes the Preview Dialog to support csv files.")
    
    module_dcs_web_preview_image = fields.Boolean(
        string="Preview Image",
        help="Extendes the Preview Dialog to support image files.")
    
    module_dcs_web_preview_mail = fields.Boolean(
        string="Preview Mail",
        help="Extendes the Preview Dialog to support mails.")
    
    module_dcs_web_preview_markdown = fields.Boolean(
        string="Preview Markdown",
        help="Extendes the Preview Dialog to support markdown files.")
    
    module_dcs_web_preview_msoffice = fields.Boolean(
        string="Preview MS Office",
        help="Extendes the Preview Dialog to support office files.")
    
    module_dcs_web_preview_rst = fields.Boolean(
        string="Preview ReStructuredText",
        help="Extendes the Preview Dialog to support reStructuredText.")
    
    module_dcs_web_preview_text = fields.Boolean(
        string="Preview Text",
        help="Extendes the Preview Dialog to support text files.")
    
    module_dcs_web_preview_vector = fields.Boolean(
        string="Preview Vector",
        help="Extendes the Preview Dialog to support vector files.")
    
    module_dcs_web_preview_video = fields.Boolean(
        string="Preview Video",
        help="Extendes the Preview Dialog to support video files.")