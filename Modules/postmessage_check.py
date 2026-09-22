# Safe static analysis only
def check_postmessage(js_content=""):
print("[*] Module 2: PostMessage Configuration Check")
# We only check code, not steal token
if "postMessage" in js_content and "access_token" in js_content:
if "event.origin" in js_content or "origin" in js_content:
print(" [✓] origin check seems present - review manually")
else:
print(" [!] postMessage sends token but origin check may be missing")
print(" Tip: Report only after manual code review, no live exploit")
else:
print(" [✓] No token in postMessage found in provided JS")

