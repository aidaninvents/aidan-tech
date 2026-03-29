# AidanOS 8

import os, datetime

os.makedirs("aidanos_notes", exist_ok=True)
LOG_FILE = "logs.txt"

def log(msg):
    with open(LOG_FILE, "a") as f:
        f.write(f"[{datetime.datetime.now()}] {msg}\n")

def calculator():
    try:
        expr = input("Calc> ")
        print("Result:", eval(expr))
        log(f"Calc used: {expr}")
    except Exception as e:
        print("Error:", e)

def notes():
    note = input("Note: ")
    with open("aidanos_notes/notes.txt", "a") as f:
        f.write(note + "\n")
    print("Saved.")
    log("Note added")

def main():
    print("Welcome to AidanOS 8")
    while True:
        cmd = input("AidanOS> ").strip().lower()

        if cmd == "exit":
            break
        elif cmd == "calc":
            calculator()
        elif cmd == "notes":
            notes()
        elif cmd == "help":
            print("Commands: calc, notes, help, exit")
        else:
            print("Unknown command")

if __name__ == "__main__":
    main()
