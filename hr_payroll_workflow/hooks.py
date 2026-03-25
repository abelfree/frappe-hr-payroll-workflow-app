app_name = "hr_payroll_workflow"
app_title = "HR Payroll Workflow"
app_publisher = "Portfolio"
app_description = "Overtime and payroll extensions for ERPNext"
app_email = "dev@example.com"
app_license = "MIT"

doc_events = {
    "Overtime Entry": {
        "on_submit": "hr_payroll_workflow.services.payroll.apply_overtime_to_salary_slip"
    }
}
