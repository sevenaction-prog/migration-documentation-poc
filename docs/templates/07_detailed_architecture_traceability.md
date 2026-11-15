# Detailed Architecture & Traceability Workbook

Use this structure when a scope requires end-to-end traceability.

## 00_Read_Me
- Purpose
- Evidence model
- Traceability rule: Source -> Decision -> BRQ -> Feature -> Rule -> Process -> Acceptance -> Story

## 01_Target_Architecture
Columns:
- Scope
- Site / space
- Library / component
- Content
- M365 object
- Access
- Status
- Rationale

## 02_Decisions
Columns:
- ID
- Decision / finding
- Status
- Impact
- Owner
- Evidence

## 03_BRQ
Columns:
- BRQ ID
- Business requirement
- Priority
- Status
- Source / evidence
- Acceptance

## 04_Features
Columns:
- Feature ID
- BRQ ID
- Feature
- Target component
- Status

## 05_Business_Rules
Columns:
- Rule ID
- Rule
- Applies to
- Status

## 06_Process_Mapping
Columns:
- Document family
- Principal process
- Interface process
- Evidence status
- Rationale

## 07_Acceptance
Columns:
- Test ID
- Scenario
- Expected result
- Status

## 08_Stories
Columns:
- Story ID
- As a
- I want
- So that
- Linked BRQ

## 09_Open_Decisions
Columns:
- ID
- Question
- Priority
- Owner
- Decision required
