"""Offline-first JSON-LD / AI-visibility evaluation. No credentials or network calls."""
from __future__ import annotations
import json
from collections import Counter
from urllib.parse import urlsplit, urlunsplit

def normalize_url(url: str) -> str:
    p = urlsplit(url.strip())
    if p.scheme not in ("https", "http") or not p.hostname:
        raise ValueError("Valid HTTP(S) citation URL required")
    path = p.path.rstrip("/") or "/"
    return urlunsplit((p.scheme.lower(), p.netloc.lower(), path, "", ""))

def validate_jsonld(markup: str, visible_facts: dict | None = None) -> dict:
    """Syntax, basic shape, and explicitly testable visible-content consistency.
    
    Does not claim full Schema.org or Google rich-result validation.
    visible_facts is an optional externally verified mapping of field names to values.
    """
    errors = []
    try:
        data = json.loads(markup)
    except (ValueError, TypeError) as ex:
        return {"valid": False, "errors": ["JSON_PARSE_ERROR: " + str(ex)]}
    nodes = data.get("@graph", [data]) if isinstance(data, dict) else data
    if not isinstance(nodes, list):
        return {"valid": False, "errors": ["ROOT_MUST_BE_OBJECT_OR_ARRAY"]}
    seen = set()
    for index, node in enumerate(nodes):
        if not isinstance(node, dict) or not node.get("@type"):
            errors.append(f"node[{index}]: missing @type")
            continue
        identifier = node.get("@id")
        if identifier:
            if identifier in seen:
                errors.append(f"node[{index}]: duplicate @id")
            seen.add(identifier)
        for key, expected in (visible_facts or {}).items():
            if key in node and node[key] != expected:
                errors.append(f"node[{index}]: {key} contradicts supplied visible fact")
    return {"valid": not errors, "errors": errors, "node_count": len(nodes),
            "scope": "JSON syntax, structure, duplicate @id and provided visible facts only"}

def measure_visibility(observations: list[dict], owned_domains: set[str]) -> dict:
    """Metrics per platform and mode. Missing/unrun tests are excluded, not zero."""
    owned = {d.lower().removeprefix("www.") for d in owned_domains}
    groups = {}
    for row in observations:
        key = (row.get("platform", "UNKNOWN"), row.get("search_mode", "UNKNOWN"),
               row.get("market", "UNKNOWN"), row.get("locale", "UNKNOWN"))
        groups.setdefault(key, []).append(row)
    results = []
    for (platform, mode, market, locale), records in sorted(groups.items()):
        attempted = [r for r in records if r.get("status") == "OBSERVED"]
        eligible = [r for r in attempted if r.get("eligible", True)]
        cited = 0
        mentioned = 0
        errors = 0
        unknown = len(records) - len(attempted)
        citation_domains = Counter()
        for r in eligible:
            mentioned += bool(r.get("brand_mentioned"))
            errors += bool(r.get("material_error"))
            target_hit = False
            for citation in r.get("citations", []):
                try:
                    hostname = urlsplit(normalize_url(citation)).hostname or ""
                except (ValueError, TypeError):
                    continue
                normalized = hostname.removeprefix("www.")
                citation_domains[normalized] += 1
                if any(normalized == d or normalized.endswith("." + d) for d in owned):
                    target_hit = True
            cited += target_hit
        n = len(eligible)
        results.append({
            "platform": platform, "search_mode": mode, "market": market, "locale": locale,
            "observations": len(records), "not_tested": unknown, "eligible": n,
            "owned_site_cited": cited, "brand_mentioned": mentioned, "material_error_responses": errors,
            "citation_coverage": round(cited / n, 4) if n else None,
            "brand_presence": round(mentioned / n, 4) if n else None,
            "material_error_rate": round(errors / n, 4) if n else None,
            "citation_domains": dict(citation_domains)
        })
    return {"groups": results, "note": "Observed sample only; not causal ranking or complete AI market share."}

def load_and_measure(path: str, owned_domains: set[str]) -> dict:
    with open(path, encoding="utf-8") as f:
        source = json.load(f)
    records = source.get("observations", [])
    if not isinstance(records, list):
        raise ValueError("observations must be a list")
    return measure_visibility(records, owned_domains)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("observations_json")
    parser.add_argument("--owned-domain", action="append", required=True)
    args = parser.parse_args()
    print(json.dumps(load_and_measure(args.observations_json, set(args.owned_domain)), indent=2))
