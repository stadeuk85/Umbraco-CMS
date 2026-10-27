# Use brand voice throughout the pipeline

**Status:** Implemented as reusable skill instructions; no live agent installation or Umbraco editing claimed.

Required skill order:
1. Resolve brand + exact culture using `skills/quintet-brand-voice/SKILL.md`.
2. Apply local voice to content creation or revision (not a final cosmetic rewrite).
3. Run `seo-geo-content-optimiser` against that content.
4. Run `schema-entity-intelligence` and `multilingual-syndication-quality` as applicable.
5. Run `eeat-financial-content-governance` with market-specific approved evidence, treating unresolved material claims as blockers.
6. Use `umbraco-draft-operator` with separate explicit authorisation only.
7. After publication by an authorised person, use `ai-visibility-citation-testing` to measure observed outcomes.

Each platform adapter (ChatGPT, Claude Cowork, Copilot Studio) must load *the same canonical version* of the group and market profiles and record `brand_profile_version` and locale in outputs. Do not assume native discovery of SKILL.md from GitHub in all products.

## Output contract for creators
brand_id, locale, group_voice_version, local_profile_version, confidence/provisional_status, format, audience, original_draft, voice_score_with_evidence, claims_needing_verification, compliance_flags, reviewer, source_ids.

## Release gate
A public-site-derived profile is PROVISIONAL. Before autonomous reuse in production, obtain signed marketing approval and bank-approved exact regulated wording and local language review. Never treat Marketing approval as a substitute for Compliance clearance.
