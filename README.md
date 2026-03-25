# Frappe HR & Payroll Workflow App

A portfolio-ready Frappe app that extends ERPNext HR with overtime capture, payroll adjustments, and approval workflows.

## Features
- Overtime submission and approval flow
- Payroll augmentation from approved overtime records
- Attendance CSV import endpoint
- Script report endpoint for overtime cost summary

## Stack
- Frappe / ERPNext
- Python
- MariaDB / PostgreSQL compatible SQL patterns

## Quick Start
1. Create a bench and get app:
   ```bash
   bench get-app hr_payroll_workflow <repo-url>
   bench --site yoursite install-app hr_payroll_workflow
   ```
2. Configure role permissions for `Overtime Entry`.
3. Call API:
   - `POST /api/method/hr_payroll_workflow.api.attendance.import_csv`
   - `GET /api/method/hr_payroll_workflow.api.reports.overtime_summary`

## Demo Data
Use `tests/sample_attendance.csv` and then submit/approve `Overtime Entry` docs.
