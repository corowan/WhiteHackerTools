# osint_search.py - Google Dorks OSINT Tool
import requests
from bs4 import BeautifulSoup
import urllib.parse
from colorama import init, Fore

init(autoreset=True)
R = Fore.RED
W = Fore.RESET

def google_dork_search(dork, num=15):
    print(f"{R}[+] Running Google Dork: {dork}{W}")
    url = "https://www.google.com/search"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    params = {"q": dork, "num": num}
    try:
        r = requests.get(url, headers=headers, params=params, timeout=15)
        soup = BeautifulSoup(r.text, "html.parser")
        results = 0
        for g in soup.find_all('div', class_='g'):
            a = g.find('a')
            if a and a.get('href') and '/url?q=' in a['href']:
                link = urllib.parse.unquote(a['href'].split('/url?q=')[1].split('&')[0])
                title_tag = a.find('h3')
                title = title_tag.text if title_tag else "No title"
                print(f"{R}├── {title}{W}\n    {link}\n")
                results += 1
        print(f"{R}[+] Found {results} results{W}")
    except Exception as e:
        print(f"{R}[!] Error: {str(e)}{W}")

def run():
    print(f"{R}╔═ OSINT Google Dorks Scanner ═╗{W}")
    dork = input(f"{R}Enter Google Dork: {W}")
    if dork.strip():
        google_dork_search(dork)
    else:
        print(f"{R}[!] Empty dork!{W}")

if __name__ == "__main__":
    run()