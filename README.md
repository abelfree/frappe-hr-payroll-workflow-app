# Frappe HR & Payroll Workflow App

[![ERPNext](https://img.shields.io/badge/ERPNext-v15-blue)](https://erpnext.com/)
[![Frappe](https://img.shields.io/badge/Frappe-Framework-green)](https://frappeframework.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

ERPNext extension focused on HR automation: overtime approval, payroll adjustment, attendance import, and cost reporting.

## Author
Abel Takele

## What This Project Demonstrates
- Custom DocType creation (`Overtime Entry`)
- Business logic hooks on document submit
- API endpoints for bulk attendance import
- SQL-backed reporting endpoint for payroll analytics

## Key Features
- Overtime submission and approval workflow
- Automatic insertion of overtime earnings into draft salary slips
- Attendance CSV import endpoint
- Overtime summary report endpoint by employee/date range

## Architecture
- `hr_payroll_workflow/hooks.py`: app hooks and doc events
- `hr_payroll_workflow/hr_payroll_workflow/services/payroll.py`: overtime-to-payroll logic
- `hr_payroll_workflow/hr_payroll_workflow/api/attendance.py`: attendance import API
- `hr_payroll_workflow/hr_payroll_workflow/api/reports.py`: overtime summary API
- `hr_payroll_workflow/hr_payroll_workflow/doctype/overtime_entry/overtime_entry.json`: custom DocType

## API Endpoints
- `POST /api/method/hr_payroll_workflow.api.attendance.import_csv`
- `GET /api/method/hr_payroll_workflow.api.reports.overtime_summary?from_date=YYYY-MM-DD&to_date=YYYY-MM-DD`

## Quick Start
```bash
bench get-app hr_payroll_workflow https://github.com/abelfree/frappe-hr-payroll-workflow-app
bench --site yoursite install-app hr_payroll_workflow
```

## Demo Flow
1. Import attendance using `tests/sample_attendance.csv`.
2. Create and submit `Overtime Entry` records.
3. Open a draft `Salary Slip` for the employee and verify overtime earning is appended.
4. Call overtime summary endpoint and review totals.

## Recruiter Notes
This repository highlights practical ERP customization, server-side automation, and ERP reporting skills relevant to Frappe/ERPNext roles.
