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

---

## 🚀 Usage

```bash
#clone
git clone https://github.com/yourusername/nessus-parser.git
#cd into directory
cd nessus-parser
#run the tool....Go!!!
python3 nessus-parser.py /path/to/folder/with/nessus/files
```

---

## 🧠 Why This Tool?

Nessus reports are powerful, but digging through XML is a pain. This tool gives you a quick and clean breakdown of the actionable network data:
- IPs to target 🎯
- Ports to exploit 💥

Perfect for:
- Pentesters  
- Red Teamers  
- SOC Analysts  
- Vulnerability Managers  
- Threat Hunters  

---

## 📜 License

MIT License. Use freely. Hack wisely. 🧠

---
