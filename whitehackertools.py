#!/usr/bin/env python3
# White Hacker Tools — Modular Version
# Framework by @wnatocry

import sys
import shutil
import os
import importlib


START_RGB = (140, 0, 0)
END_RGB   = (255, 70, 70)

TOOLS_DIR = os.path.join(os.path.dirname(__file__), "tools")
if not os.path.exists(TOOLS_DIR):
    os.makedirs(TOOLS_DIR, exist_ok=True)


def rgb_interp(a, b, t):
    return int(a + (b - a) * t)

def red_gradient(text):
    out = []
    chars = [c for c in text if c != "\n"]
    total = max(1, len(chars) - 1)
    idx = 0

    for ch in text:
        if ch == "\n":
            out.append("\n")
            continue

        t = idx / total
        r = rgb_interp(START_RGB[0], END_RGB[0], t)
        g = rgb_interp(START_RGB[1], END_RGB[1], t)
        b = rgb_interp(START_RGB[2], END_RGB[2], t)

        out.append(f"\033[38;2;{r};{g};{b}m{ch}\033[0m")
        idx += 1

    return "".join(out)

def center(text):
    try:
        w = shutil.get_terminal_size((80, 20)).columns
    except:
        w = 80
    return "\n".join(line.center(w) for line in text.splitlines())


def print_banner():
    try:
        import banner
        banner_text = banner.BANNER
        byline = banner.BYLINE
    except Exception as e:
        banner_text = "HACKER TOOLS"
        byline = "by @wnatocry"

    print(red_gradient(center(banner_text)))
    print(red_gradient(center(byline)))
    print()


MENU = """
┌───────────────────────────────────────────────────────┐
│ [1] OSINT Search (Number / FML / Nickname)            │
│ [2] Nickname Intelligence                             │
│ [3] Number Lookup                                     │
│ [4] FML Identity Scan                                 │
│ [5] Network Recon                                     │
│ [6] Utility Tools                                     │
│ [7] Scan-ports                                        │
│ [8] Exit                                              │
└───────────────────────────────────────────────────────┘
"""

def print_menu():
    print(red_gradient(center(MENU)))


def safe_run(module_name):
    try:
        module_path = f"tools.{module_name}"
        mod = importlib.import_module(module_path)
        if hasattr(mod, "run"):
            mod.run()
        else:
            print(red_gradient("[!] Module exists but missing run() function\n"))
    except ModuleNotFoundError:
        print(red_gradient(f"[!] Module '{module_name}' not found\n"))
    except Exception as e:
        print(red_gradient(f"[ERROR] {e}\n"))


def main():
    ACTIONS = {
        "1": lambda: safe_run("osint_search"),
        "2": lambda: safe_run("nickname_intel"),
        "3": lambda: safe_run("number_lookup"),
        "4": lambda: safe_run("fml_scan"),
        "5": lambda: safe_run("network_recon"),
        "6": lambda: safe_run("utility_tools"),
        "7": lambda: safe_run("scan_ports"),
        "8": lambda: exit_app(),

    }

    while True:
        os.system("cls" if os.name == "nt" else "clear")

        print_banner()
        print_menu()

        choice = input("\033[97m[>] \033[0m").strip()

        if choice in ACTIONS:
            ACTIONS[choice]()
        else:
            print(red_gradient("\n[!] Invalid option.\n"))

        input("\033[97mPress ENTER to return...\033[0m")


def exit_app():
    print(red_gradient("\nBye!\n"))
    sys.exit(0)

if __name__ == "__main__":
    main()
