# Structural consistency assurance - Assessment & Decision Guide
> Reusable fictional template inspired by a structural assurance workbench. Not a certificate or approved assurance opinion.

## Executive question
Can the organization demonstrate that a business relationship remains valid as information crosses systems, transformations, actors and time? A working component does not prove its business relations remain valid.

## Scope and boundary
Included: objects, identifiers, cardinalities, states, authority, time, change paths, invariants and evidence. Excluded without separate work: entire application quality, compliance certification and physical security.

## Intake protocol
Accept candidate data from SQL DDL, data catalog, JSON Schema, OpenAPI, CSV relation register or model manifest. Capture source, format, version, owner and confidentiality. Parsing creates candidates, not verified business meaning. Owners must confirm semantics.

## Model of relationships
Represent entity, identifier, relation, cardinality, authority, state, time validity and consumers. Ask whether a target record preserves the same meaning as its source record.

## End-to-end transformations
For each relationship, trace events through API, queues, ETL and human handoffs. Identify where a reference may be dropped, its timestamp overwritten, a status incorrectly defaulted or an approval detached from its subject.

## Invariant definition
Each invariant has ID, business assertion, criticality, scope, establishment test, preservation test, evidence, owner and result. Example: downstream activation of case A must retain the decision authorizing case A. A status flag without decision ID is insufficient proof.

## Test strategy
Establishment means the relationship was valid initially. Preservation means it remained valid at every relevant boundary. Results are PASS, FAIL, INSUFFICIENT EVIDENCE or NOT TESTED. A good average score does not override a failed critical invariant.

## Findings and recovery
Document business impact, affected flow, suspected root cause, source, required evidence, action owner, priority, correction, re-test and sign-off. A correction task is not itself assurance evidence.

## Executive report
Explain scope, covered relations, critical failures, unknowns, limitations and conditions for a decision. Keep reasoning linked to the evidence index.

## Handover and acceptance
Supply model register, transformations, invariants, tests, findings, decisions and provenance. All critical invariants require an owner and a tested conclusion. Do not upload actual schemas, source files or personal records to a public library.