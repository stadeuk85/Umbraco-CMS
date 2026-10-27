"""Read-only Umbraco CMS Delivery API client, with explicit host allowlisting.

Not a Management API or draft-writing client. Delivery API must be enabled by the owner.
"""
from __future__ import annotations
import json
from urllib.request import Request, urlopen
from urllib.parse import quote, urlsplit
from uuid import UUID

class UmbracoDeliveryReader:
    def __init__(self, base_url: str, allowed_host: str, timeout: int = 15):
        p = urlsplit(base_url)
        if p.scheme != "https" or p.hostname != allowed_host or p.username or p.password:
            raise ValueError("HTTPS base URL must match exact allowlisted host")
        if p.path not in ("", "/") or p.query or p.fragment:
            raise ValueError("Base URL must be origin only")
        self.origin = f"https://{allowed_host}" + (f":{p.port}" if p.port else "")
        self.timeout = timeout

    def content_by_id(self, content_id: str, culture: str = "en-GB") -> dict:
        UUID(content_id)  # Reject path injection and ambiguous node selectors
        if not culture or len(culture) > 35 or not all(c.isalpha() or c == "-" for c in culture):
            raise ValueError("Invalid culture")
        path = "/umbraco/delivery/api/v2/content/item/" + quote(content_id, safe="")
        req = Request(self.origin + path, headers={
            "Accept": "application/json", "Accept-Language": culture
        }, method="GET")
        with urlopen(req, timeout=self.timeout) as response:
            if response.status != 200:
                raise RuntimeError(f"Delivery API HTTP {response.status}")
            if "json" not in response.headers.get("Content-Type", ""):
                raise ValueError("Non-JSON Delivery API response")
            data = json.load(response)
        if not isinstance(data, dict):
            raise ValueError("Unexpected Delivery API content shape")
        return {"source": "umbraco_delivery_api_v2", "culture": culture,
                "content_id": content_id, "published": True, "data": data,
                "limitations": ["Published delivery content only", "No document type authoring or draft writes"]}

    def draft_write(self, *args, **kwargs):
        raise PermissionError("Read-only reader. Draft writing requires an independently implemented, audited Management API adapter.")
