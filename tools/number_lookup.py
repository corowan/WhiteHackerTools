# number_lookup.py - Phone Number OSINT
import requests
from colorama import init, Fore

init(autoreset=True)
R = Fore.RED
W = Fore.RESET

def lookup_number(phone):
    phone = phone.replace(" ", "").replace("-", "")
    print(f"{R}[+] Looking up: {phone}{W}")
    url = f"https://htmlweb.ru/json/phone/{phone.lstrip('+')}"
    try:
        r = requests.get(url, timeout=12)
        data = r.json()
        if "error" not in str(data) and data:
            info = data.get("0", data)
            print(f"{R}├── Country: {info.get('country_name', 'N/A')}{W}")
            print(f"{R}├── Region: {info.get('region', 'N/A')}{W}")
            print(f"{R}├── Operator: {info.get('oper', 'N/A')}{W}")
            print(f"{R}├── Type: {info.get('line', 'N/A')}{W}")
        else:
            print(f"{R}[!] Not found or invalid number{W}")
    except Exception as e:
        print(f"{R}[!] Request failed: {e}{W}")

def run():
    print(f"{R}╔═ Phone Number Lookup ═╗{W}")
    phone = input(f"{R}Enter phone (+79991234567): {W}").strip()
    if phone:
        lookup_number(phone)
    else:
        print(f"{R}[!] Empty input!{W}")

if __name__ == "__main__":
    run()