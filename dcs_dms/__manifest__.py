# -*- encoding: utf-8 -*-

{
    "name": "Dcs Documents",
    "summary": """Document Management System""",
    "version": '11.0.2.1.6',   
    "category": 'Document Management',   
    "license": "AGPL-3",
    "author": "E.andrianina",
    "contributors": [
        "E.Andrianina",
    ],
    "depends": [
        "web",
        "mail",
        "base_setup",
        "dcs_utils",
        "dcs_security",
        "dcs_web_utils",
        "dcs_web_preview",
        "dcs_web_client",
        "dcs_web_client_refresh",
        "dcs_web_preview_audio",
        "dcs_web_preview_image",
    ],
    "data": [
        "security/dms_security.xml",
        "security/ir.model.access.csv",
        "template/assets.xml",
        "views/dms_menu.xml",
        "views/dms_documents_view.xml",
        "views/dms_tag_view.xml",
        "views/dms_category_view.xml",
        "views/dms_settings_view.xml",
        "views/dms_directory_view.xml",
        "views/dms_file_view.xml",
        "views/dms_data_view.xml",
        "views/res_config_settings_view.xml",
    ],
    "demo": [
        "demo/dms_user_demo.xml",
        "demo/dms_tag_demo.xml",
        "demo/dms_category_demo.xml",
        "demo/dms_settings_demo.xml",
        "demo/dms_directory_demo.xml",
        "demo/dms_file_demo.xml",
    ],
    "qweb": [
        "static/src/xml/*.xml",
    ],
    "images": [
        'static/description/banner.png'
    ],
    "external_dependencies": {
        "python": [],
        "bin": [],
    },
    "application": True,
    "installable": True,
}