---
name: schema-entity-intelligence
description: Generate, validate and maintain evidence-backed schema.org JSON-LD and a governed entity registry for Umbraco; no invented bank entity claims or automatic publication.
version: 1.0.0
---
# Schema and Entity Intelligence

## Trigger
Structured data, JSON-LD, Schema.org, article/person/organisation entities, authors, legal entity identities, service page markup, breadcrumbs, schema audit, metadata consistency.

## Inputs
Exact content ID, locale, canonical URL, rendered page, Umbraco field aliases and node version, authoritative entity registry, approved role and legal entity records; URL and website access permissions.

## Workflow
1. Snapshot page and collect existing JSON-LD, visible text, canonical, byline, dates, breadcrumb and entity references. Do not fabricate markup from generic brand names.
2. Resolve the entity registry by legal entity ID + jurisdiction + locale. Separate group/brand, legal entities, regulated activities, people, editorial authors, service offerings and individual branch offices. An approved named owner must verify legal entity URLs, registered name, regulator, address, identifiers and sameAs links.
3. Choose applicable vocabulary: Organization or relevant subtype, WebSite/WebPage, Article/BlogPosting, Person, BreadcrumbList, and service-related types only where semantically correct. FAQ structured data only if page contains the exact eligible content and platform guidelines permit it. Never imply special rich result eligibility.
4. Generate JSON-LD @graph with stable page/entity identifiers. Use absolute canonical URLs and consistent inLanguage, headline, datePublished/dateModified and author/publisher references. Do not supply financial product returns, awards, ratings or credentials without evidence.
5. Run JSON syntax validation, schema vocabulary inspection and applicable search-engine-specific validation. Check markup represents facts actually visible to readers, verify URLs resolve and no duplicate contradictory @id.
6. Compare schema with visible content, metadata, author cards, source documents and locale-specific legal disclosures. Pass financial statements to governance skill.
7. Output exact Umbraco alias diff, approved data source IDs, validation findings, risk and preview. Only write an unpublished draft via umbraco-draft-operator on explicit authority.

## Output
content_id, culture, source_version, entity_registry_version, schema_before, schema_after, assertion_evidence_map, validators_run, validator_results, page_schema_consistency, unresolved_claims, proposed_field_changes, approval_required, draft_write_status.

## Negative tests
Wrong legal entity for a local market => BLOCKER.
Missing credential source => omit or mark UNKNOWN.
Author not visible on article => do not silently invent it in JSON-LD.
Schema passes syntax but disagrees with visible page => BLOCKER.
Incorrect sameAs cross-brand link => do not emit.
No rich result after valid markup => not evidence of failure; eligibility and display are distinct.
Reference: https://developers.google.com/search/docs/appearance/structured-data/sd-policies
