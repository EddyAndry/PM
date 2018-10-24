# -*- encoding: utf-8 -*-

{
    "name": "Dcs Automation Extension",
    "summary": """Extension for Odoo's Base Automation""",
    "version": '11.0.1.0.1',   
    "category": 'Extra Tools',   
    "license": "AGPL-3",
    "author": "E.Andrianina",
    "contributors": [
        "E.andrianina>",
    ],
    "depends": [
        "base_automation",
    ],
    "data": [
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
