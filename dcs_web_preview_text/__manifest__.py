# -*- encoding: utf-8 -*-

{
    "name": "Dcs Preview Text",
    "summary": """Text Preview""",
    "version": "11.0.2.0.1",
    "category": "Extra Tools",
    "license": "AGPL-3",
    "author": "E.andrianina",
    "contributors": [
        "E.andrianina",
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