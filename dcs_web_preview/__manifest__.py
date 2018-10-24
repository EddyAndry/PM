# -*- encoding: utf-8 -*-

{
    "name": "Dcs Preview",
    "summary": """File Preview Dialog""",
    "version": "11.0.2.1.4",
    "category": "Extra Tools",
    "license": "AGPL-3",
    "author": "E.Andrianina",
    "contributors": [
        "E.Andrianina",
    ],
    "depends": [
        "web",
        "base_setup",
        "dcs_web_utils",
    ],
    "data": [
        "template/assets.xml",
        "views/res_config_settings_view.xml",
    ],
    "demo": [
        "demo/preview_demo.xml",
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