# 🔍 Nessus Parser - IP & Port Extractor

**Nessus Parser** is a simple yet powerful Python tool that automates the extraction of IP addresses and their associated open TCP ports from `.nessus` files. It’s built for pentesters, red teamers, vulnerability managers, and anyone who wants quick access to actionable host data from Nessus scan results.

---

## 🛠 Features

✅ Parses **all `.nessus` files** in a specified folder  
✅ Outputs clean, deduplicated list of IPs and their open TCP ports  
✅ Skips hosts with only port `0`  
✅ Generates:
- `output.txt` — List of IPs and their open TCP ports  
- `clean_ips.txt` — Clean list of IPs only  

---

## 📂 Sample Output

### `output.txt`
