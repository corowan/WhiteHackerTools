# fml_scan.py - Fast Directory Brute Force
import requests
import threading
from queue import Queue
from colorama import init, Fore

init(autoreset=True)
R = Fore.RED
W = Fore.RESET

WORDLIST = ["admin","login","wp-admin","phpmyadmin","backup","config","test","uploads",".git","cgi-bin","admin.php","dashboard","robots.txt","sitemap.xml","server-status"]

def dir_worker(base_url, q):
    while True:
        path = q.get()
        if path is None: break
        url = f"{base_url.rstrip('/')}/{path.lstrip('/')}"
        try:
            r = requests.get(url, timeout=6, allow_redirects=True, headers={"User-Agent": "Mozilla/5.0"})
            if r.status_code in [200, 301, 302, 403]:
                size = len(r.content)
                print(f"{R}[+] {r.status_code} → {url} ({size} bytes){W}")
        except:
            pass
        q.task_done()

def fml_scan(target):
    if not target.startswith("http"):
        target = "http://" + target
    print(f"{R}[+] Scanning directories: {target}{W}")
    q = Queue()
    for _ in range(30):
        t = threading.Thread(target=dir_worker, args=(target, q))
        t.daemon = True
        t.start()
    for word in WORDLIST:
        q.put(word)
    q.join()
    print(f"{R}[+] Directory scan completed!{W}")

def run():
    print(f"{R}╔═ Directory Brute Force Scanner ═╗{W}")
    url = input(f"{R}Target URL: {W}").strip()
    if url:
        fml_scan(url)
    else:
        print(f"{R}[!] URL required!{W}")

if __name__ == "__main__":
    run()