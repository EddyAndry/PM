# -*- encoding: utf-8 -*-

{
    "name": "Dcs Preview CSV",
    "summary": """CSV Preview""",
    "version": "11.0.2.0.1",
    "category": "Extra Tools",
    "license": "AGPL-3",
    "author": "MuK IT",
    "contributors": [
        "E.Andrianina",
    ],
    "depends": [
        "dcs_web_preview",
    ],
    "data": [
        "template/assets.xml",
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