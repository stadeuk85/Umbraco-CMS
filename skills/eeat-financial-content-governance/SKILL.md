---
name: eeat-financial-content-governance
description: Evidence-based editorial trust, provenance, expertise and regulated financial content review for Umbraco draft changes across jurisdictions. Routes regulatory decisions to authorised humans.
version: 1.0.0
---
# E-E-A-T and Financial Content Governance

## Activation
Use for author attribution, author profiles, reliability, trust checks, financial article review, bank disclosures, fact checking, content syndication, localisation, regulated claims, or whenever the SEO/GEO optimiser requests release gates.

## Principle
E-E-A-T is a useful quality framework, not a single calculable Google ranking factor or certification. Trust is central: content must be accurate, verifiable, transparent and suitable for its reader. Financial and investment material requires higher scrutiny. This skill never makes legal or regulatory determinations.

## Sources and precedence
1. Current approved policy, legal entity disclosures, mandatory wording, product terms and jurisdiction-specific compliance rules supplied by the organisation.
2. Authoritative primary sources for law, supervision and technical facts; preserve effective dates.
3. Named internal subject-matter expert verified by the organisation.
4. Publicly published information for background only.
Where sources disagree, pause and escalate; do not silently select whichever fits the copy. Do not guess Brown Shipley/Quintet regulatory permissions, regulator registration, financial figures or product characteristics.

## Review workflow
1. Record entity, market, language, page type, intended audience, promotion status and reviewer identity.
2. Create a **claim register**: claim_id, exact_text, type (fact/opinion/forward-looking/promotion), citation, effective_date, source_owner, verification_status.
3. Check evidence freshness: calendar-specific tax rules, financial limits, return data, manager roles, mandates and regulatory descriptors require explicit as-of dates and authoritative support.
4. Confirm expertise signals where relevant: attributable byline, verified current role, accessible biography, editorial review ownership and publication/update dates. Never invent titles, memberships or experience.
5. Confirm transparent risk framing: distinguish information from personalised advice; preserve required warnings and qualifications; avoid exaggerated certainty or unsubstantiated comparisons, superiority and performance claims.
6. Check provenance of re-used and syndicated material: attribution, canonical strategy, original publication, translation accuracy, source links, context and local disclosures. Never erase named authors without an approved reason.
7. Cross-check article body, teaser, Open Graph, schema JSON-LD, author metadata and any variants for contradictions.
8. Issue independent **editorial** and **compliance escalation** outcomes; route regulated sign-off to named authorised reviewer. Do not conflate compliance approval with model assessment.
9. Generate evidence-linked review with blockers and exact remediation actions.

## Severity and release gates
- BLOCKER: unsupported material financial promise, incorrect legal entity/regulator assertion, missing mandated disclaimer, leaked non-public data, unapproved regulated promotion, stale or conflicting high-impact financial number. No draft promotion to publication.
- MAJOR: missing expert attribution where material, material translation ambiguity, broken cited primary-source link, unverified time-sensitive claim; reviewer remediation needed.
- MINOR: metadata consistency, language clarity, optional trust cues; advisory.
- UNKNOWN: insufficient evidence; never turn UNKNOWN into PASS by score averaging.

Publication requires required editorial owner plus any jurisdictional legal/compliance sign-offs in the organisation's own workflow. Automated agents can propose and save draft changes only with permission; they cannot assert approval on a person's behalf.

## Required review artifact
entity, jurisdiction, locale, content_id, source_version, claim_register[], byline_status, source_link_checks[], disclaimer_checks[], editorial_findings[], compliance_escalations[], severity, reviewer_required, approved_to_publish=false.
Provide a clear version-specific audit trail, immutable change diff and rollback instructions.

## Acceptance tests
- UK Budget/allowance numbers without year/source => BLOCKER or MAJOR, never silently filled.
- A source document says "investment values may fall"; rewrite must not weaken the warning.
- Syndicated article loses a credited author's profile link => flag MAJOR.
- An article is anonymous but correctly owned by a corporate editorial function => assess evidence, not an automatic fail.
- No reliable compliance source => UNKNOWN and request human review.
