{
    "name": "HR Employee Name Extended",
    "version": "18.0.4.0.0",
    "category": "Human Resources",
    "summary": "Structured first/last/nickname with locale-aware formatting, inverse writes, and robust search",
    "description": """
        Enterprise-grade name management for hr.employee with:
        - Structured fields: first_name, last_name, nick_name (safe, opinionated defaults)
        - Locale-aware formatting via system parameters (western/asian/custom)
        - Stored computed legal name and friendly display name
        - Inverse on 'name' to keep first/last synchronized for external writes
        - Optimized name search across all fields with proper DB indexes
        - Validation, migration hooks, and concurrency-safe updates

        Designed for Odoo 18 Enterprise. No circular sync with res.users/res.partner
        unless explicitly enabled via context.
    """,
    "author": "Chris Busillo (Shiny Computers)",
    "website": "",
    "maintainers": ["cbusillo"],
    "depends": [
        "hr",
        "base_setup",
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/hr_employee_views.xml",
        "views/res_config_settings_views.xml",
        "data/server_actions.xml",
        "data/menu.xml",
    ],
    "post_init_hook": "post_init_hook",
    "installable": True,
    "application": False,
    "license": "LGPL-3",
}
