# -*- encoding: utf-8 -*-

{
    "name": "Dcs Web Client",
    "summary": """Odoo Web Client Extension""",
    "version": "11.0.2.0.2",
    "category": "Extra Tools",
    "license": "AGPL-3",
    "author": "E.Andrianina",
    "contributors": [
        "E.Andrianina",
    ],
    "depends": [
        "web",
        "bus",
        "base_setup",
        "dcs_web_utils",
    ],
    "data": [
        "template/assets.xml",
        "views/res_config_settings_view.xml",
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
    "application": False,
    "installable": True,
    
}