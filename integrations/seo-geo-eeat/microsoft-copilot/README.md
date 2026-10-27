# Microsoft Copilot / Copilot Studio deployment adapter

SKILL.md files are canonical source instructions; they are **not** assumed to be auto-discovered by Microsoft 365 Copilot.

## Copilot Studio agent mapping
- Agent instructions: behaviour, scope, source precedence, evidence status taxonomy and human-approval gates from both skills.
- Knowledge: selected, access-controlled approved policies and content source registry; observe data access entitlements.
- Actions: a governed custom connector, agent flow or MCP tools exposing the read/propose/write-draft contract.
- Power Automate / approvals: human approval captured through the organisation's accepted workflow, outside model text.
- Audit: record user, target node, locale, source version, changed aliases, approver and observed result.
- Environment: build first in a non-production tenant with test pages, then assess DLP and compliance policies.

## Guardrails
Avoid raw broad network calls, unscoped CMS credentials, autonomous publication, or direct production write access through general-purpose prompts. The integration layer must enforce restrictions server-side rather than relying only on agent instructions.

## Acceptance walkthrough
Read a known staging article; produce SEO/GEO proposal; run trust review; request approver; write version-checked draft; read it back; compare; verify it remains unpublished. Test a denial for an unapproved user, stale version and out-of-scope locale.
