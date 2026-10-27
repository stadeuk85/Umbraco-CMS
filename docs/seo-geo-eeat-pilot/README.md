# Search visibility content pilot: cross-platform skills

**Status:** implementation package for review; no connection to an Umbraco backoffice established and no CMS changes executed.

## Goal
Use one consistent review method across ChatGPT, Claude Cowork and Microsoft Copilot: SEO/GEO content suggestions, evidence and E-E-A-T assurance, then human-approved *draft-only* writes to Umbraco.

## Reuse architecture
- Shared source of truth: `skills/seo-geo-content-optimiser/SKILL.md`, `skills/eeat-financial-content-governance/SKILL.md`, `skills/umbraco-draft-operator/SKILL.md`.
- ChatGPT: project instructions or reusable prompt wrapping the same skills; use a connected tool or computer-use session for actual CMS operations.
- Claude/Cowork: install skill folders in an approved skills location and expose configured MCP server tools; never assume skill text grants CMS permissions.
- Microsoft Copilot: map skill steps into Copilot Studio agent instructions, knowledge sources and approved tool actions; do not assume native SKILL.md discovery. Test connector entitlements in the target tenant.
- Integration layer: an approved organisation-hosted MCP gateway / Umbraco API proxy (or browser fallback) that enforces roles, field allowlists, locale allowlists, versions, audit logging and editor approval.
- Private enterprise content: store confidential source documents, source IDs, internal compliance policies and pilot evaluations in an approved private store, **not this public repository**.

## Small UK pilot
Start with a representative set of up to ten approved UK content nodes, spanning service pages, commentary and author profiles. Select nodes only after Marketing and Compliance confirm access, ownership and source currency. For each node, capture source version, copy, structured data, actual canonical/hreflang, attribution and approved evidence. Evaluate baseline, propose edits, run governance, stage draft, obtain human sign-off and measure after publishing via approved workflow.

## Metrics and evidence
1. **Mechanical quality:** title, meta, content hierarchy, internal links, schema validity, alt text, attribution and canonical/hreflang; report tested numerator/denominator.
2. **Editorial quality:** evidence coverage, major/blocker counts, reviewer acceptance rate, content fidelity and harmful-change rate.
3. **Delivery:** time from proposal to reviewed draft, stale-write prevention, field verification and rollback readiness.
4. **Search outcomes:** Search Console impressions, clicks and coverage where authorised; avoid conflating technical readiness with ranking.
5. **AI answer visibility:** a fixed, versioned prompt set across explicitly named public search products, timestamps, region, model, retrieval mode, source citations, exact brand fact accuracy and citation rate. ChatGPT or Claude general chat without search is not equivalent to their search features.

## Phases
P0: confirm Umbraco version, API capabilities, tenant permissions, approved compliance material, source registry and UK page IDs.
P1: readonly extract + before/after proposals + evidence checks; human review.
P2: add draft-write adapter on a least-privileged sandbox/staging instance, concurrency safeguards and automated readback.
P3: supervised production drafting (not publishing), monitoring and audit evidence.
P4: expansion into group-wide locales and entity-specific rules once UK pilot gates pass.

## Release criteria
Zero false claims of completed write; zero unauthorised publishes; 100% proposed material factual claims traceable to reviewed source; no unreviewed BLOCKER; draft readback matches proposed allowed fields; all review approvals captured outside the model; pass adversarial tests.
