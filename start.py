import os
import sys
import subprocess
import time
import importlib

R = "\033[91m"
W = "\033[0m"

def animate(text):
    for i in range(4):
        print(f"\r{R}{text}{'.' * i}   {W}", end="")
        time.sleep(0.6)
    print(f"\r{R}{text}... Done{W}")

os.system("cls" if os.name == "nt" else "clear")

animate("Checking libraries")
missing = []
for mod in ["requests", "beautifulsoup4", "colorama"]:
    try:
        importlib.import_module(mod)
    except:
        missing.append(mod)

if missing:
    print(f"{R}Installing libraries{W}")
    for pkg in missing:
        subprocess.check_call([sys.executable, "-m", "pip", "install", pkg], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

print(f"{R}Launching program{W}")
time.sleep(0.8)

if os.path.exists("whitehackertools.py"):
    subprocess.call([sys.executable, "whitehackertools.py"])
else:
    print(f"{R}Error: whitehackertools.py not found{W}")
    time.sleep(2)