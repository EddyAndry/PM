

{
    "name": "Dcs Security",
    "summary": """Security Features""",
    "version": "11.0.1.1.1",
    "category": "Extra Tools",
    "license": "AGPL-3",
    "author": "E.Andrianina",
    "contributors": [
        "E.Andrianina",
    ],
    "depends": [
        "dcs_utils",
        "dcs_autovacuum",
    ],
    "data": [
        "security/security.xml",
        "security/ir.model.access.csv",
        "views/lock.xml",
        "views/groups.xml",
        "data/autovacuum.xml",
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
    "post_load": "_patch_system",
}