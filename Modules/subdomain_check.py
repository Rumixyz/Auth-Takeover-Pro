# Safe DNS existence check only
import socket

def check_subdomain(domain):
print(f"[*] Module 3: Subdomain Existence Check for {domain}")
try:
socket.gethostbyname(domain)
print(" [✓] Domain exists - not claimable")
except socket.gaierror:
print(" [!] Domain does NOT resolve (NXDOMAIN)")
print(" Tip: It MAY be claimable, but do NOT claim. Report as 'potentially claimable' only if program allows")

