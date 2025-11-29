# network_recon.py - Domain/IP Recon
import socket
from colorama import init, Fore

init(autoreset=True)
R = Fore.RED
W = Fore.RESET

def recon(target):
    print(f"{R}[+] Recon target: {target}{W}")
    try:
        ip = socket.gethostbyname(target)
        print(f"{R}├── IP: {ip}{W}")
        print(f"{R}├── Shodan: https://shodan.io/host/{ip}{W}")
        print(f"{R}├── Censys: https://search.censys.io/hosts/{ip}{W}")
        print(f"{R}├── FOFA: https://fofa.info/result?qbase64={target}{W}")
    except:
        print(f"{R}[!] Cannot resolve hostname{W}")

def run():
    print(f"{R}╔═ Network Recon Tool ═╗{W}")
    target = input(f"{R}Domain or IP: {W}").strip()
    if target:
        recon(target)
    else:
        print(f"{R}[!] Empty target!{W}")

if __name__ == "__main__":
    run()