from modules.redirect_check import check_redirect
from modules.postmessage_check import check_postmessage
from modules.subdomain_check import check_subdomain

print("=== Auth-Takeover-Pro - Safe Mode ===")
url = input("Enter URL: ")
check_redirect(url)
check_postmessage("sample js code with postMessage")
# Example: check_subdomain("expired.example.com")

print("\n[Done] All checks are safe detection only. For authorized testing only.")

