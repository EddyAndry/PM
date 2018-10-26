# -*- encoding: utf-8 -*-

{
    "name": "Dcs Large Objects Field Widget",
    "summary": """PGSQL Large Objects Field Widget""",
    "version": '11.0.1.0.1',   
    "category": 'Extra Tools',   
    "license": "AGPL-3",
    "author": "MuK IT",
    "contributors": [
        "E.Andrianina",
    ],
    "depends": [
        "web",
        "dcs_fields_lobject",
    ],
    "data": [
        "template/assets.xml"
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
    "auto_install": True,
    "application": False,
    "installable": True,
}
