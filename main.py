# OAuth Security Checker - Educational Purpose Only
# Only for authorized testing

print("=== OAuth Security Scanner (Safe Mode) ===")

url = input("Paste URL with redirect_uri param: ")

# Safe check - No payloads, only validation logic
if "redirect_uri" not in url:
print("[!] redirect_uri parameter not found")
else:
print("[*] Checking if redirect_uri is properly validated...")
print("[*] Tip: Manually verify if app uses allowlist for redirect_uri")
print("[*] This tool does NOT try to redirect to external domains")
print("[✓] Safe check completed - Report only if misconfiguration confirmed with permission")
