# nickname_intel.py - Username OSINT (Sherlock style)
import requests
import time
from colorama import init, Fore

init(autoreset=True)
R = Fore.RED
W = Fore.RESET

SITES = {
    "GitHub": "https://github.com/{}",
    "Twitter/X": "https://twitter.com/{}",
    "Instagram": "https://instagram.com/{}",
    "Reddit": "https://reddit.com/user/{}",
    "VK": "https://vk.com/{}",
    "Steam": "https://steamcommunity.com/id/{}",
    "LinkedIn": "https://linkedin.com/in/{}",
    "TikTok": "https://tiktok.com/@{}",
    "Pinterest": "https://pinterest.com/{}",
}

def check_nickname(username):
    print(f"{R}[+] Searching username: {username}{W}")
    found = 0
    for site, url in SITES.items():
        link = url.format(username)
        try:
            r = requests.get(link, timeout=8, headers={"User-Agent": "Mozilla/5.0"})
            if r.status_code == 200 and username.lower() in r.text.lower():
                print(f"{R}├── [+] {site}: {link}{W}")
                found += 1
            else:
                print(f"{R}├── [-] {site}{W}")
        except:
            print(f"{R}├── [!] {site} (error/timeout){W}")
        time.sleep(0.6)
    print(f"{R}[+] Total profiles found: {found}{W}")

def run():
    print(f"{R}╔═ Username OSINT Scanner ═╗{W}")
    nick = input(f"{R}Enter username: {W}").strip()
    if nick:
        check_nickname(nick)
    else:
        print(f"{R}[!] Username cannot be empty!{W}")

if __name__ == "__main__":
    run()