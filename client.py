#!/usr/bin/env python3
"""client.py
Zero-dependency Python client for website-contact-extractor.
Runs synchronously against Apify Cloud and returns dataset items.
"""

import os
import sys
import json
import urllib.request
import urllib.error
from typing import Dict, Any, List, Optional

ACTOR_SLUG = "website-contact-extractor"
DEFAULT_BASE_URL = f"https://api.apify.com/v2/acts/deepaksheoran172~{ACTOR_SLUG}/run-sync-get-dataset-items"

def run_website_contact_extractor(
    payload: Dict[str, Any],
    apify_token: Optional[str] = None,
    timeout_sec: int = 120
) -> List[Dict[str, Any]]:
    """Executes website-contact-extractor on Apify Cloud synchronously.
    
    Args:
        payload: The input JSON dictionary matching the actor input schema.
        apify_token: Apify API token. Defaults to os.environ.get('APIFY_TOKEN').
        timeout_sec: Network timeout in seconds (default 120).
        
    Returns:
        List of result items from the default dataset.
    """
    token = apify_token or os.environ.get("APIFY_TOKEN")
    if not token:
        raise ValueError(
            "Apify token is required. Pass apify_token argument or set APIFY_TOKEN environment variable."
        )

    url = f"{DEFAULT_BASE_URL}?token={token}"
    data_bytes = json.dumps(payload).encode("utf-8")
    
    req = urllib.request.Request(
        url,
        data=data_bytes,
        headers={"Content-Type": "application/json"},
        method="POST"
    )

    try:
        with urllib.request.urlopen(req, timeout=timeout_sec) as response:
            if response.status not in (200, 201):
                raise RuntimeError(f"Actor run returned HTTP {response.status}: {response.read().decode('utf-8')}")
            raw_body = response.read().decode("utf-8")
            return json.loads(raw_body)
    except urllib.error.HTTPError as e:
        err_msg = e.read().decode("utf-8") if e.fp else str(e)
        raise RuntimeError(f"HTTPError {e.code} calling {ACTOR_SLUG}: {err_msg}") from e
    except urllib.error.URLError as e:
        raise RuntimeError(f"URLError connecting to Apify: {e.reason}") from e


if __name__ == "__main__":
    sample_payload = {
    "startUrls": [
        "https://stripe.com",
        "https://linear.app"
    ]
}
    
    token = os.environ.get("APIFY_TOKEN")
    if not token:
        print("[!] APIFY_TOKEN not set in environment.")
        print("To run against live Apify cloud:")
        print("  export APIFY_TOKEN='your_token'")
        print("  python client.py")
        print("
Demonstrating constructed request:")
        print(f"Endpoint: {DEFAULT_BASE_URL}")
        print(f"Payload: {json.dumps(sample_payload, indent=2)}")
        sys.exit(0)

    print(f"[*] Running {ACTOR_SLUG} with payload...")
    try:
        items = run_website_contact_extractor(sample_payload, apify_token=token)
        print(f"[+] Success! Received {len(items)} dataset items:")
        print(json.dumps(items[:3], indent=2))
    except Exception as e:
        print(f"[-] Execution failed: {e}")
        sys.exit(1)
