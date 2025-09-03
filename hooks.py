from odoo.api import Environment

from .models.hr_employee import NameFormatter


def _initialize_employee_names(env: Environment) -> None:
    Employee = env["hr.employee"].sudo()
    icp = env["ir.config_parameter"].sudo()
    fmt = (icp.get_param("user_name_extended.format") or "western").strip().lower()

    domain = ["|", ("first_name", "=", False), ("last_name", "=", False)]
    offset = 0
    step = 200
    while True:
        employees = Employee.search(domain, limit=step, offset=offset, order="id")
        if not employees:
            break
        for employee in employees:
            first = (employee.first_name or "").strip()
            last = (employee.last_name or "").strip()
            if not first or not last:
                parsed = NameFormatter.split_full_name(employee.name or "", fmt)
                vals = {}
                if not first and parsed.get("first_name"):
                    vals["first_name"] = parsed["first_name"]
                if not last and parsed.get("last_name"):
                    vals["last_name"] = parsed["last_name"]
                if vals:
                    employee.with_context(skip_name_propagation=True).write(vals)
            if not employee.nick_name and employee.first_name:
                employee.with_context(skip_name_propagation=True).write({"nick_name": employee.first_name})
        if len(employees) < step:
            break
        offset += step


def post_init_hook(env: "Environment") -> None:
    _initialize_employee_names(env)
