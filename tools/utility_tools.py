# utility_tools.py - Hash & Encoding Tools
import hashlib
import base64
from colorama import init, Fore

init(autoreset=True)
R = Fore.RED
W = Fore.RESET

def run():
    print(f"{R}╔══════════ Utility Tools ══════════╗{W}")
    print(f"{R}1. MD5 Hash          2. SHA256 Hash{W}")
    print(f"{R}3. Base64 Encode     4. Base64 Decode{W}")
    choice = input(f"{R}Choose [1-4]: {W}").strip()
    text = input(f"{R}Enter text: {W}").strip()

    if choice == "1":
        print(f"{R}[+] MD5: {hashlib.md5(text.encode()).hexdigest()}{W}")
    elif choice == "2":
        print(f"{R}[+] SHA256: {hashlib.sha256(text.encode()).hexdigest()}{W}")
    elif choice == "3":
        print(f"{R}[+] Base64: {base64.b64encode(text.encode()).decode()}{W}")
    elif choice == "4":
        try:
            print(f"{R}[+] Decoded: {base64.b64decode(text).decode()}{W}")
        except:
            print(f"{R}[!] Invalid Base64!{W}")
    else:
        print(f"{R}[!] Wrong option{W}")

if __name__ == "__main__":
    run()