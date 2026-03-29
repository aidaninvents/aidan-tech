# AidanOS10.12 — Basic Python OS (LTS)
import os, datetime

LOG_FILE = "logs.txt"

def log(action):
    with open(LOG_FILE, "a") as f:
        f.write(f"[{datetime.datetime.now()}] {action}\n")

def version():
    print("AidanOS10.12 — Basic Python OS (LTS)")
    log("Checked version")

def main():
    print("Welcome to AidanOS10.12 — LTS")
    while True:
        cmd = input("AidanOS> ").strip().split()
        if not cmd: continue
        if cmd[0] == "help":
            print("Commands: help, echo, clear, version")
        elif cmd[0] == "echo":
            print(" ".join(cmd[1:]))
        elif cmd[0] == "clear":
            print("\033[H\033[J", end="")
        elif cmd[0] == "version":
            version()
        else:
            print("Unknown command:", cmd[0])

if __name__ == "__main__":
    main()