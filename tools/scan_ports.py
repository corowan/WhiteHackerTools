# scan_ports.py - Fast TCP Port Scanner
import socket
import threading
from colorama import init, Fore

init(autoreset=True)
R = Fore.RED
W = Fore.RESET

PORTS = [21,22,23,25,53,80,110,135,139,143,443,993,995,1723,3389,5900,8080,8443,10000]

def scan(ip, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.7)
        if s.connect_ex((ip, port)) == 0:
            service = {21:"FTP",22:"SSH",80:"HTTP",443:"HTTPS",3389:"RDP",3306:"MySQL"}.get(port, "")
            print(f"{R}[+] Port {port}/tcp OPEN  → {service}{W}")
        s.close()
    except:
        pass

def port_scan(target):
    try:
        ip = socket.gethostbyname(target)
        print(f"{R}[+] Scanning {target} → {ip}{W}")
        for port in PORTS:
            threading.Thread(target=scan, args=(ip, port), daemon=True).start()
        threading.Event().wait(5)
        print(f"{R}[+] Scan finished!{W}")
    except:
        print(f"{R}[!] Host not resolved{W}")

def run():
    print(f"{R}╔═ Fast Port Scanner ═╗{W}")
    host = input(f"{R}Target host: {W}").strip()
    if host:
        port_scan(host)
    else:
        print(f"{R}[!] Host required!{W}")

if __name__ == "__main__":
    run()