![Auth-Takeover-Pro Banner]cd436a15-4446-d736-d482-3a4ca95ec64e.jpeg

Auth-Takeover-Pro - OAuth Security Scanner (For Authorized Testing Only)

> ⚠️ **Disclaimer:** This tool is for educational purposes and authorized Bug Bounty programs only. Do not use on targets without permission.

### What it does (Safe Detection Only)
- Checks if redirect_uri is properly validated
- Detects potential postMessage misconfigurations via static code analysis
- Flags redirect URIs pointing to non-existent subdomains for manual review

### How to Use
python main.py --url https://target.com

This tool only reports potential issues, it does NOT steal tokens or takeover accounts.

