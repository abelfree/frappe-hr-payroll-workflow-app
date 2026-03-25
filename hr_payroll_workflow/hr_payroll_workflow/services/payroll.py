from __future__ import annotations

import frappe


def apply_overtime_to_salary_slip(doc, _method=None):
    """Attach approved overtime amount into the next draft salary slip."""
    slip_name = frappe.db.get_value(
        "Salary Slip",
        {
            "employee": doc.employee,
            "docstatus": 0,
            "start_date": ("<=", doc.overtime_date),
            "end_date": (">=", doc.overtime_date),
        },
        "name",
    )

    if not slip_name:
        frappe.log_error(
            title="Overtime pending payroll",
            message=f"No draft Salary Slip found for {doc.employee} on {doc.overtime_date}",
        )
        return

    slip = frappe.get_doc("Salary Slip", slip_name)
    overtime_amount = float(doc.approved_hours or 0) * float(doc.hourly_rate or 0)

    slip.append(
        "earnings",
        {
            "salary_component": "Overtime",
            "amount": overtime_amount,
        },
    )
    slip.flags.ignore_validate_update_after_submit = True
    slip.save()
