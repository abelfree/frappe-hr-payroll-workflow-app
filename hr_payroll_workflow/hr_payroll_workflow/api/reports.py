from __future__ import annotations

import frappe


@frappe.whitelist()
def overtime_summary(from_date: str, to_date: str):
    rows = frappe.db.sql(
        """
        SELECT employee, SUM(approved_hours) AS hours,
               SUM(approved_hours * hourly_rate) AS amount
        FROM `tabOvertime Entry`
        WHERE docstatus = 1
          AND overtime_date BETWEEN %(from_date)s AND %(to_date)s
        GROUP BY employee
        ORDER BY amount DESC
        """,
        {"from_date": from_date, "to_date": to_date},
        as_dict=True,
    )
    return {"data": rows}
