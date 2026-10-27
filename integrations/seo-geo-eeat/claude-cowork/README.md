# Claude Cowork deployment adapter

## Installation concept
Copy or selectively package the three `skills/*/SKILL.md` folders in an organisation-approved skills location. The main optimisation and governance skills operate on supplied text even without CMS access; draft writing requires a connected MCP server or supervised computer-use session.

## Configuration
- Enable retrieval from the private approved source repository using enterprise access controls.
- Offer tool names equivalent to `umbraco_read_content`, `umbraco_read_content_type`, `umbraco_propose_draft`, `umbraco_write_draft`, `umbraco_read_draft`.
- Require person-specific least privilege, precise node/locale scope, version-checked writes, approval reference and write logs.
- Never allow a workflow to skip governance because it was invoked as "just SEO".
- Recheck authentication state and verify the resulting draft by reading it back.

## Operational prompt
"Read the SEO/GEO content optimiser skill and E-E-A-T financial content governance skill. Assess content using approved evidence, produce proposed alias-level changes and record blockers. Only use the draft operator after explicit permission. Do not publish."
