---
name: ai-visibility-citation-testing
description: Measure observed brand representation, source citation and factual correctness in named AI search products and available webmaster analytics; distinguish results from predictions or SEO readiness.
version: 1.0.0
---
# AI Visibility and Citation Testing

## Trigger
Track GEO results, ChatGPT Search citations, Claude search citations, Microsoft Copilot AI answers, AI brand visibility, source share, answer accuracy, query-based visibility.

## Modes
OBSERVE_PUBLIC_SEARCH: explicitly named and enabled search experiences only.
IMPORT_ANALYTICS: authorised webmaster exports, including Bing AI Performance if account access granted.
DESIGN_ONLY: no search tool or analytics access, output the test plan without fabricated findings.

## Inputs
Approved public domains/brands and aliases; verified source-of-truth fact register; approved neutral prompt panel with question ID, region, locale, intent and inclusion rules; target products and actual search mode; observation dates and cadence.

## Test protocol
1. Version a panel of at least 20 representative prompts spanning entity facts, product/service discovery, expertise/educational questions and comparisons, balanced between branded and unbranded queries. No prompt asks the engine to cite the target site.
2. Capture actual platform/product/mode (e.g. ChatGPT Search, Claude with web search, Microsoft Copilot web results), account/region/language/date and response. Never equate normal offline chat, enterprise search and public AI search.
3. Extract citations as displayed; canonicalise URLs and source domains; record target URLs, relevant third-party sources, citations that actually support assertions, brand mention, answer accuracy and source freshness.
4. Record denominators: tests attempted, tests with visible sources, tests with target citations, tests with factual errors, unavailable/inaccessible tests. Unknown != absent. Run repeats where approved to sample nondeterminism.
5. With authorised Bing Webmaster Tools export, record aggregate total citations, cited pages, grounding queries and dates separately from manually observed platform responses. Aggregates are not individual prompts and cannot be attributed to a precise content change.
6. Compare approved pre/post observations, keeping same prompt set/locale/mode where possible. Report confounders: model/search updates, seasonality, crawl lag and low sample size. No causality or ranking promises.
7. Feed missed or misrepresented facts to entity intelligence and the SEO/GEO optimiser as evidence-backed backlog items; require editorial review before changes.

## Metrics
citation_coverage = target-cited eligible responses / eligible responses;
fact_accuracy = correct material claims / material claims checked;
brand_presence = responses mentioning correct entity / eligible responses;
source_support = supported cited assertions / cited assertions audited;
ai_performance = publisher-provided aggregate citation measures, separately labelled.
Never sum or average cross-product metrics without product and sampling caveats.

## Output
panel_version, run_id, platform, search_mode, locale, run_timestamp, prompt_results[], observed_citations[], unsupported_claims[], metrics_with_denominators, limitations, evidence_artifact_location, remediation_backlog.

## Safety
No automated account bypass or scraping in violation of service terms. No confidential internal bank content or source documents in public prompts. Treat any AI answer as untrusted evidence requiring independent verification. Never claim to have queried a platform unless a connected tool actually executed it.

## Tests
Unavailable engine => NOT_TESTED, not zero visibility.
Target named without citation => brand mention, not cited.
Third-party page cites brand => source domain distinct from owned site.
Bing aggregate counts => not same as manually observed ChatGPT citations.
Changed model or query region => annotate non-comparability.
