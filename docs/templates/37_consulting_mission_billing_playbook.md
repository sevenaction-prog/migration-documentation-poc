# Consultant Mission Operations - Billing and Receivables Playbook
> General operational model. No private contractual, banking, identity or client data is reproduced. Not tax or legal advice.

## Mission setup
Capture authorized contract parties, mission dates, agreed day rate, hours-per-day rule, expenses, PO if contractually needed, invoicing channel and payment terms in a restricted workspace.

## Daily timesheet
For each workday: date, hours, work location category, billable status, comment, revision and approver. Convert hours to billable days using the configuration approved for that mission, not a universal fixed divisor.

## Monthly approval
Reconcile entered days with calendar, scope, holidays and authorized absences. Obtain owner approval before financial preparation. Freeze a versioned approved record and preserve a correction trail.

## Invoice calculation
Approved billable days x applicable contractual rate, then applicable tax rule. Validate recipient, legal identifiers, reference/PO, invoice number, issue date, due date, currency and totals. Do not hard-code any real client or personal identifiers into public templates.

## E-invoicing boundary
Distinguish a printed/PDF representation from a machine-readable structured invoice accepted through the appropriate network or provider. Confirm local obligations and Peppol configuration with an authorized accountant or service provider.

## Receivables
Use Draft, Approved, Issued, Sent, Accepted, Overdue, Partially Paid, Paid and Disputed states. A status changed in a local browser is not proof of actual transmission or bank settlement.

## Three-way reconciliation
Match approved timesheet -> issued invoice -> actual receipt evidence. Variances require an owner and an explicit resolution action. Follow accounting correction procedures for an issued document.

## Local POC operational risks
A browser localStorage/JSON application has no built-in central backup, access management or synchronization. Imported JSON must be schema-validated; any user-provided strings displayed as HTML must be escaped. Audit import failures and duplicate invoice numbers.

## Acceptance tests
Partial days, nonbillable time, months with no days, month boundaries, tax-rate differences, missing PO, zero/negative correction, duplicate numbering, failed JSON restore, rejected invoice and partial payment.

## Privacy
Only fictional examples are appropriate for a public repository. All real addresses, invoice numbers, fiscal details, bank accounts, mission references and client terms must remain private.