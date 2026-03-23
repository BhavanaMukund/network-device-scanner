from scapy.all import ARP, Ether, srp
import requests

def get_vendor(mac):
    try:
        url = f"https://api.macvendors.com/{mac}"
        r = requests.get(url, timeout=3)
        if r.status_code == 200:
            return r.text
        else:
            return "Unknown"
    except:
        return "Unknown"


def scan_network(ip_range):
    devices = []

    arp = ARP(pdst=ip_range)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")

    packet = ether / arp

    result = srp(packet, timeout=3, verbose=0)[0]

    for sent, received in result:
        mac = received.hwsrc
        vendor = get_vendor(mac)

        devices.append({
            "ip": received.psrc,
            "mac": mac,
            "vendor": vendor
        })

    return devices
