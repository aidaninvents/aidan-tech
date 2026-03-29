# AidanOS 3 H2 LTS (2018)

import os, datetime

# Setup
os.makedirs("aidanos_notes", exist_ok=True)
os.makedirs("aidanos_files", exist_ok=True)
LOG_FILE = "logs.txt"

def log(msg):
    with open(LOG_FILE, "a") as f:
        f.write(f"[{datetime.datetime.now()}] {msg}\n")

# Apps
def calculator():
    try:
        expr = input("Calc> ")
        print("Result:", eval(expr))
        log(f"Calc used: {expr}")
    except Exception as e:
        print("Error:", e)

def notes():
    note = input("Write note: ")
    with open("aidanos_notes/notes.txt", "a") as f:
        f.write(f"[{datetime.datetime.now()}] {note}\n")
    print("Saved.")
    log("Note added")

def files():
    print("Files:", os.listdir("aidanos_files"))

# Shell
def main():
    print("Welcome to AidanOS 3 H2 LTS (2018)")
    while True:
        cmd = input("AidanOS3> ").strip().lower()

        if cmd == "exit":
            break
        elif cmd == "calc":
            calculator()
        elif cmd == "notes":
            notes()
        elif cmd == "files":
            files()
        elif cmd == "help":
            print("Commands: calc, notes, files, help, exit")
        else:
            print("Unknown command")

if __name__ == "__main__":
    main()
