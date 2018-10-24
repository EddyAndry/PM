# -*- encoding: utf-8 -*-

{
    "name": "Dcs Autovacuum",
    "summary": """Configure automatic garbage collection""",
    "version": "11.0.2.1.3",
    "category": "Extra Tools",
    "license": "AGPL-3",
    "author": "E.andrianina",
    "contributors": [
        "E.Andrianina",
    ],
    "depends": [
        "base",
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/rules.xml",
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
    "auto_install": False,
    "application": False,
    "installable": True,
    "post_init_hook": '_init_default_rules',
}