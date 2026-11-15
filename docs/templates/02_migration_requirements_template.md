# Migration Requirements Template

## Confidence model
Use consistently:
- **CONFIRMED** — explicit decision or directly observed fact.
- **RECOMMENDED** — supported analyst proposal.
- **TO VALIDATE** — insufficient evidence or business decision required.

## 0. Reading guide / arbitration
Summarize blocking decisions and evidence quality.

## 1. Purpose, objectives and scope
Define business outcomes, scope boundaries and measurable coverage.

## 2. AS-IS findings and limits
Document repositories, folder patterns, systems of record, duplication, lifecycle folders, sensitive zones and evidence gaps.

## 3. Guiding principles
Ownership before location. One authoritative reference. Metadata over status folders when justified. Do not recreate master systems.

## 4. Target functional architecture
Describe target sites, libraries, document sets, lists and interfaces.

## 5. Classification and metadata
Define common and library-specific metadata, mandatory fields and controlled values.

## 6. Enterprise process alignment
Map document families to the approved enterprise process taxonomy. Keep interfaces separate.

## 7. Workflows and lifecycle
Describe document lifecycle, statuses, approvals and publication.

## 8. Business Requirements
| BRQ ID | Requirement | Evidence | Status | Acceptance |
|---|---|---|---|---|
| BRQ-001 | Users can retrieve authoritative documents without knowing the legacy path. | Inventory + workshop | RECOMMENDED | Representative search scenarios pass |
| BRQ-002 | Sensitive content is invisible to unauthorized users. | Security decision | TO VALIDATE | Negative access tests pass |
| BRQ-003 | Every migrated item is reconciled to a source or approved disposition. | Migration control | CONFIRMED | Reconciliation = 100% |

## 9. Business rules
Define ownership, lifecycle, duplication, archival and source-of-truth rules.

## 10. Security, confidentiality and retention
Define role groups, restricted zones, negative tests, classification and retention validation.

## 11. Integrations and master systems
Clarify what remains in source systems and what SharePoint stores as evidence.

## 12. Non-functional requirements
Searchability, performance expectations, auditability, accessibility and supportability.

## 13. Delivery and migration strategy
Waves, pilot, remediation, mapping, reconciliation, cutover and hypercare.

## 14. Acceptance and Go/No-Go
Define test scenarios and exit criteria.

## 15. Governance
Define Business Owner, Process Owner, M365 team, Security, Records and Migration responsibilities.

## 16. Open decision register
| ID | Decision | Priority | Owner | Status |
|---|---|---|---|---|
| D-001 | Confirm target ownership by document family | P0 | Business Owner | TO VALIDATE |
| D-002 | Confirm retention rules | P0 | Records / Legal | TO VALIDATE |
| D-003 | Confirm restricted access groups | P0 | Security / Business | TO VALIDATE |

## Annex A. Sources & evidence
## Annex B. Workshop validation questions
## Annex C. Validation sheet / next iteration
