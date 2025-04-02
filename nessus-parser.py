import os
import xml.etree.ElementTree as ET
from collections import defaultdict
import argparse
from glob import glob

def extract_ips_and_ports_from_file(filepath):
    ip_ports = defaultdict(set)

    try:
        tree = ET.parse(filepath)
        root = tree.getroot()
    except ET.ParseError as e:
        print(f"[!] Failed to parse {filepath}: {e}")
        return ip_ports

    for report_host in root.findall(".//ReportHost"):
        ip = report_host.get("name")
        if not ip:
            continue

        for item in report_host.findall(".//ReportItem"):
            port = item.get("port")
            protocol = item.get("protocol")

            if port and protocol == "tcp":
                ip_ports[ip].add(int(port))

    return ip_ports

def merge_and_clean_ip_ports(all_ip_ports):
    merged = defaultdict(set)

    for ip_dict in all_ip_ports:
        for ip, ports in ip_dict.items():
            merged[ip].update(ports)

    # Remove entries where only port 0 is present
    cleaned = {
        ip: ports for ip, ports in merged.items()
        if not (len(ports) == 1 and 0 in ports)
    }

    return cleaned

def save_output(ip_ports, folder_path):
    output_path = os.path.join(folder_path, "output.txt")
    clean_ips_path = os.path.join(folder_path, "clean_ips.txt")

    with open(output_path, "w") as f1, open(clean_ips_path, "w") as f2:
        for ip, ports in sorted(ip_ports.items()):
            port_list = sorted(ports)
            f1.write(f"{ip}:{','.join(str(p) for p in port_list)}\n")
            f2.write(f"{ip}\n")

    print(f"[+] output.txt saved to: {output_path}")
    print(f"[+] clean_ips.txt saved to: {clean_ips_path}")

def main():
    parser = argparse.ArgumentParser(description="Process all .nessus files in a folder and extract IPs and open ports.")
    parser.add_argument("path", help="Path to the folder containing .nessus files")

    args = parser.parse_args()
    folder_path = args.path

    if not os.path.isdir(folder_path):
        print(f"[-] Invalid directory: {folder_path}")
        return

    nessus_files = glob(os.path.join(folder_path, "*.nessus"))
    if not nessus_files:
        print("[!] No .nessus files found in the directory.")
        return

    all_ip_ports = []

    for file in nessus_files:
        print(f"[+] Processing: {file}")
        ip_ports = extract_ips_and_ports_from_file(file)
        all_ip_ports.append(ip_ports)

    cleaned_ip_ports = merge_and_clean_ip_ports(all_ip_ports)
    save_output(cleaned_ip_ports, folder_path)

if __name__ == "__main__":
    main()
