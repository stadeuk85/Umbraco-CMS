# Executable pilot runtime (Python standard library)

This is executable, read-only reference code to accompany the five SEO/GEO/E-E-A-T skills. **It is not a configured live Umbraco gateway, an MCP server, nor an integrated AI search API client.**

## What works now
- `umbraco_delivery_reader.py`: HTTPS-only, exact-host allowlisted published-content retrieval by GUID and locale through Umbraco Delivery API v2, if enabled on the instance. Deliberately blocks draft writes.
- `visibility_pipeline.py`: evaluate JSON-LD shape, duplicate IDs and supplied visible facts; compute observed source citation/brand mention/error rates by actual platform, mode, market and locale from collected JSON.
- `tests/test_visibility_pipeline.py`: runnable offline tests with no accounts or proprietary inputs.

## Run
From repository root: `python -m unittest discover -s runtime/tests -v`

Example visibility command:
`python -m runtime.visibility_pipeline runtime/examples/observations.synthetic.json --owned-domain example.org`

## Important boundaries
1. **No live credentials or calls made.** The domain allowlist is mandatory for the optional content read.
2. Delivery API behaviour/availability depends on Umbraco version and project settings; verify the instance's API specification before connecting. Draft edits require a separately implemented **Management API** adapter and human authorisation.
3. `validate_jsonld` does not replace JSON Schema, Schema.org semantic validation, live page matching or Google Rich Results Test.
4. The observations JSON must contain **real test runs** before the resulting metrics can be called measurements. No platform search is automated here, and simulated examples are labelled synthetic.
5. Security review is required before production use; the reference reader does not currently provide enterprise OAuth, proxy policy or response-size enforcement.
