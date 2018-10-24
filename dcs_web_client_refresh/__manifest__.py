

{
    "name": "Dcs Web Refresh",
    "summary": """Web Client Refresh""",
    "version": "11.0.2.1.3",
    "category": "Extra Tools",
    "license": "AGPL-3",
    "author": "E.Andrianina",
    "contributors": [
        "E.Andrianina",
    ],
    "depends": [
        "base_automation",
        "dcs_automation_extension",
        "dcs_web_client",
    ],
    "data": [
        "template/assets.xml",
        "views/refresh_action_view.xml",
        "views/res_config_settings_view.xml",
        "data/refresh_actions.xml",
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