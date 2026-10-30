# Website Contact & Executive Extractor MCP Server & Python API

[![Apify Store](https://img.shields.io/badge/Apify_Store-Run_on_Apify-blue?style=for-the-badge&logo=apify)](https://apify.com/deepaksheoran172/website-contact-extractor)
[![MCP Server](https://img.shields.io/badge/MCP-Model_Context_Protocol-purple?style=for-the-badge)](https://modelcontextprotocol.io)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)
[![Hub](https://img.shields.io/badge/Live_Catalog-B2B_Scrapers_Hub-emerald?style=for-the-badge)](https://deepakshe.github.io/b2b-mcp-apify-scrapers-hub/)

> **Crawl corporate domains for verified emails, LinkedIn company profiles, Twitter/X, and executive contacts. MCP Server & Python SDK.**

---

## ⚡ The Problem vs. The Solution

Finding decision makers across corporate websites takes hours of manual navigation. This crawler systematically indexes About Us, Team, and Contact pages to extract executive names, corporate emails, telephone numbers, and social links.

- **Zero-Proxy Architecture:** Pure asynchronous execution designed for extreme speed (<50MB RAM).
- **Multi-Interface Support:** Run via pure Python SDK, Node.js fetch, n8n / Make.com workflow, or Claude / Cursor MCP Agent.
- **Production Reliable:** Backed by Apify's serverless infrastructure with 99.9% uptime SLA.

---

## 🚀 Quickstart: Pure Python (Zero-Dependency)

No third-party SDKs required. Run directly with Python standard library:

```python
import json
import os
import urllib.request

APIFY_TOKEN = os.getenv("APIFY_TOKEN", "YOUR_APIFY_TOKEN")
ACTOR_URL = "https://api.apify.com/v2/acts/deepaksheoran172~website-contact-extractor/run-sync-get-dataset-items?token=" + APIFY_TOKEN

payload = {
  "startUrls": [
    "https://stripe.com",
    "https://linear.app"
  ]
}

req = urllib.request.Request(
    ACTOR_URL,
    data=json.dumps(payload).encode("utf-8"),
    headers={"Content-Type": "application/json"},
    method="POST"
)

with urllib.request.urlopen(req, timeout=120) as resp:
    results = json.loads(resp.read().decode("utf-8"))
    print(f"Retrieved {len(results)} items:")
    print(json.dumps(results[:2], indent=2))
```

---

## 🌐 Quickstart: Node.js / TypeScript

```javascript
const APIFY_TOKEN = process.env.APIFY_TOKEN || 'YOUR_APIFY_TOKEN';
const ACTOR_URL = `https://api.apify.com/v2/acts/deepaksheoran172~website-contact-extractor/run-sync-get-dataset-items?token=${APIFY_TOKEN}`;

const payload = {
  "startUrls": [
    "https://stripe.com",
    "https://linear.app"
  ]
};

async function run() {
  const res = await fetch(ACTOR_URL, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(payload)
  });
  const items = await res.json();
  console.log(`Received ${items.length} records:`, items.slice(0, 2));
}

run().catch(console.error);
```

---

## 🤖 Claude Desktop & Cursor MCP Server Setup

Add this actor to your `claude_desktop_config.json` to allow Claude / Cursor AI agents to execute it autonomously:

```json
{
  "mcpServers": {
    "website-contact-extractor": {
      "command": "npx",
      "args": ["-y", "@apify/actors-mcp-server"],
      "env": {
        "APIFY_TOKEN": "YOUR_APIFY_TOKEN",
        "ACTOR_NAME": "deepaksheoran172/website-contact-extractor"
      }
    }
  }
}
```

---

## 🔄 n8n & Make.com Automation

A fully configured production n8n workflow template is bundled in this repository as [`workflow.json`](./workflow.json).

1. In n8n, click **Workflow** -> **Import from File...** and select `workflow.json`.
2. Provide your `APIFY_TOKEN` in the environment variables or HTTP Request node.
3. Schedule it to run daily or trigger on demand from webhooks.

---

## 📊 Output Schema Highlights

Each returned item includes normalized, RFC-compliant fields:
- `url`
- `emails`
- `phones`
- `linkedin_url`
- `twitter_url`
- `github_url`

---

## 🏷️ Pricing & 60% Launch Discount

- **Apify Store:** Available under pay-per-result pricing with a **60% Launch Discount**.
- **Run Online:** Test it instantly on the [Apify Store Console](https://apify.com/deepaksheoran172/website-contact-extractor).
- **Fleet Hub:** Explore all 62 enterprise scrapers and MCP servers at [b2b-mcp-apify-scrapers-hub](https://deepakshe.github.io/b2b-mcp-apify-scrapers-hub/).

---

## 📄 License

MIT License. Free for personal, commercial, and enterprise integration.
