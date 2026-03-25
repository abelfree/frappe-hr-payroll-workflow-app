from __future__ import annotations

import csv
from io import StringIO

import frappe


@frappe.whitelist(methods=["POST"])
def import_csv(content: str):
    """Import minimal attendance records from raw CSV text."""
    reader = csv.DictReader(StringIO(content))
    created = 0

    for row in reader:
        att = frappe.get_doc(
            {
                "doctype": "Attendance",
                "employee": row["employee"],
                "attendance_date": row["attendance_date"],
                "status": row.get("status", "Present"),
            }
        )
        att.insert(ignore_permissions=True)
        created += 1

    frappe.db.commit()
    return {"created": created}
