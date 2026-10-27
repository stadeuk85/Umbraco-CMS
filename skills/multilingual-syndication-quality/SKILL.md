---
name: multilingual-syndication-quality
description: Validate and propose controlled fixes to locale variants, canonical and hreflang signals, authorship, syndicated content, translations and financial disclosures in Umbraco.
version: 1.0.0
---
# Multilingual and Syndication Quality

## Trigger
Translated financial pages, regional bank sites, syndication, locale variants, canonical/hreflang, byline drift, duplicate-content errors or regional disclosure mismatches.

## Inputs
Content node family IDs, exact market and locale codes, per-page URL and CMS version, published DOM and HTTP headers, locale routing map, canonical strategy, original syndicated story identity, approved terminology and legal disclosures.

## Workflow
1. Identify the source article, each local-market adaptation and translated variant. Never assume a translation exists just because URLs share a slug.
2. Fetch each page's actual status, indexability, canonical, rendered hreflang, page title, article byline/profile link, source link, original publication date, and locale-sensitive disclosure.
3. Build a reciprocal hreflang adjacency matrix for existing equivalent pages, check valid language-region tags, self-references, return links and optionally x-default. Preserve independent canonicals for genuine translations; flag any canonical that incorrectly consolidates distinct language variants.
4. Compare essential facts and claims across variants: numbers, dates, people, product terms, legal entity references, risk statements, contact information and approved local terms. Do not replace jurisdiction-specific requirements with group-global copy.
5. Verify syndication attribution: original source, named author, current expert profile when supported, publication/update dates and approved source acknowledgement; distinguish legitimate anonymous corporate copy from lost attribution.
6. Raise BLOCKER for changed regulated meaning/incorrect legal entity or missing legally mandated warnings; MAJOR for lost author attribution, broken reciprocity or unsupported material translation.
7. Produce proposed locale-specific field corrections with linked evidence and no implicit writes. Route final variants for local editorial/compliance review, then draft operator.

## Output
content_family, locales_checked, coverage_matrix, canonical_matrix, hreflang_errors, author_provenance, claim_differences, local_disclosure_findings, locale_specific_proposals, blockers, human_approvers, readback_plan.

## Safety
No automatic machine-translation publication; do not invent pages for missing locales; never overwrite existing editor updates; always evaluate market-specific financial promotion rules. Preserve audit trail and rollback pointers.

## Tests
Single missing reciprocal hreflang => report exact pair.
English and Dutch pages canonically point to English despite distinct content => flag.
One syndicated variant drops expert attribution => flag MAJOR.
Mandatory local-market disclaimer altered by translation => BLOCKER.
