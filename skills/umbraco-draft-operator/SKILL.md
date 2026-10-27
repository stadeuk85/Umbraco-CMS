---
name: umbraco-draft-operator
description: Safely stage approved field-level Umbraco edits as version-checked drafts through authorised tools or controlled computer use; never publish without a separate human approval workflow.
version: 1.0.0
---
# Umbraco Draft Operator

## Required operating modes
READ_ONLY (default), PROPOSE, WRITE_DRAFT. Never enter WRITE_DRAFT without an explicit authorised user instruction for the content ID and locale. Publication, template changes, role modifications and bulk operations are out of scope for this skill.

## Contract for tool backends
read_content(node_id, culture) -> node_id, version_or_etag, content_type, fields_by_alias, variants, updated_at
read_schema(content_type) -> editable aliases, editors, validation, allowed cultures
create_draft(node_id, culture, expected_version, changes, idempotency_key) -> draft_id, version, preview_url?
read_draft(draft_id) -> saved fields and version
compare_draft(draft_id, source_version) -> diff
list_approvals(draft_id) -> recorded human approvals, never assume
All write tools must be least-privileged, allowlisted, logged, rate-limited and backed by server-side optimistic concurrency. Tool names here are **interfaces**, not a claim that real endpoints exist.

## Draft flow
1. Confirm target instance, editor's rights, website, culture, content ID and branch/release.
2. Read node, document type and permitted fields. Never infer field aliases from display names.
3. Freeze snapshot with version/ETag and hash of selected fields; confirm no contradictory concurrent edit.
4. Verify optimisation proposal, governance findings and operator scope; reject unsupported aliases, cross-locale writes, disallowed media or schema fields.
5. Show exact diff and obtain authorisation specific to the draft write.
6. Use deterministic idempotency key keyed by node, culture, source version and proposed diff hash.
7. Write as **unpublished draft** only; immediately read back and compare all changed fields. If UI-driven, verify visible save status and page state; if verification fails, report UNKNOWN.
8. Return draft identifier, fields, preview URL if provided, source version, saved version, audit reference and rollback path.
9. If tools unavailable, output a manual checklist and machine-readable change proposal; do not imply the CMS was updated.

## Computer-use fallback
Access Umbraco backoffice only within an authenticated session delegated by a human. Navigate to a confirmed node; avoid guessing identical page titles. Screenshot/read each before and after state. Never click Publish, Unpublish, Delete, Move, permission, access, user or deployment controls. Stop on session expiry, popups requesting credentials/MFA, ambiguous save state or validation error. No copying credentials to chat or logs.

## Failure behaviour
409/etag mismatch: no retry with blind overwrite; re-read and re-review.
403: stop, report missing permission.
Validation errors: return exact failing aliases, never bypass.
Partial updates: compare server state and reverse only using explicitly supported undo with user instruction.
