from odoo import models
from .hr_employee import NameFormatter


class _NameSyncMixin(models.AbstractModel):
    _name = "_name_sync.mixin"
    _description = "Name sync helpers"

    def _sync_name_to_employees_common(self, new_name: str, employee_domain: list) -> None:
        if not new_name:
            return
        employees = self.env["hr.employee"].sudo().search(employee_domain)
        if not employees:
            return
        icp = self.env["ir.config_parameter"].sudo()
        fmt = (icp.get_param("user_name_extended.format") or "western").strip().lower()
        parsed = NameFormatter.split_full_name(new_name, fmt)
        if not parsed.get("first_name"):
            return
        for emp in employees:
            vals = {
                "first_name": parsed.get("first_name", emp.first_name),
                "last_name": parsed.get("last_name", emp.last_name or "Unknown"),
            }
            emp.with_context(skip_name_propagation=True).write(vals)
