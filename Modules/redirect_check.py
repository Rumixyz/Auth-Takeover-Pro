# Safe detection only
def check_redirect(url):
print("[*] Module 1: Redirect Validation Check")
if "redirect_uri" not in url:
print(" -> redirect_uri param not found")
return

# Safe logic: check if url contains multiple domains or @ symbol which is risky
# No actual redirection attempt
if "@" in url or url.count("http") > 1:
print(" [!] Potential risky redirect pattern found - Needs manual verification")
print(" Tip: Verify on HackerOne target if allowlist is used")
else:
print(" [✓] No obvious risky pattern - still verify allowlist manually")

