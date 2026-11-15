# Target SharePoint Architecture

## Purpose
Short business-facing target architecture for a document migration scope.

## Cover fields
| Field | Value |
|---|---|
| Business area | [Business Area] |
| Scope | [Scope Name] |
| Business owner | [To confirm] |
| Workshop participants | [Roles / Teams] |
| Evidence base | Inventory + workshop notes + process references |

## 1. Introduction
Summarize the scope, evidence level and major design decision.

## 2. Architecture principles
- Classify by real business ownership, not by legacy folder path.
- SharePoint is the target document repository.
- Collaboration tools are entry points, not separate document stores by default.
- Do not recreate source-of-truth applications in SharePoint.
- Limit each library to the most useful metadata set.

## 3. Proposed target architecture
| Library / space | Primary content | Recommended access |
|---|---|---|
| Operational Documents | Active business evidence and working documents | Business team; restricted subsets when required |
| Reference & Templates | Approved templates, procedures and reference material | Controlled contributors; broad read access |
| Restricted Cases | Sensitive individual or case-based evidence | Named business roles only |
| Archive | Closed or historical content retained under approved rules | Read-only / records access |

## 4. Library detail
For each library, document:
- purpose
- principal content families
- document set / grouping logic
- Top 7 metadata
- access model
- lifecycle
- source-of-truth boundary

### Default Top 7 metadata example
1. DocumentType
2. BusinessCategory
3. Status
4. Owner
5. ReferenceDate
6. BusinessReference
7. Classification

## 5. Common metadata foundation
| Metadata | Purpose |
|---|---|
| DocumentType | Controlled business document type |
| BusinessCategory | Functional navigation axis |
| Status | Lifecycle state |
| Owner | Single accountable business owner |
| ReferenceDate | Business-effective date |
| BusinessReference | Case / campaign / contract reference |
| Classification | Access / sensitivity classification |

## 6. Sensitive information
Use library- or site-level security boundaries where inherited permissions cannot safely meet access needs.

## 7. Site navigation
Home / Operational Documents / Reference & Templates / Restricted Cases / Archive

## 8. Recommended views
Active / To review / By owner / By category / Archived

## 9. Decisions to confirm
- Target site / workspace
- Library security boundaries
- Retention by family
- Master systems
- Collaboration entry point

## 10. Migration recommendation
Do not rebuild the legacy folder tree automatically. Preserve, rationalize or replace folders only when supported by evidence and business decision.

## 11. Sources and assumptions
List inventory files, workshop notes, process references and explicit decisions.

## 12. Conclusion
Summarize the target architecture, key controls and remaining decisions in five lines or fewer.
