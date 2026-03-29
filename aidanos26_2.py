aidanos26_1_full.py
# AidanOS26.1 — Full Python OS in ONE file

import os, time, datetime, socket, random

# --- Configuration ---
UPDATE_SERVER = "127.0.0.1"  # Server IP
UPDATE_PORT = 12345
LOG_FILE = "logs.txt"
DATA_FILE = "data.txt"

# --- Logging ---
def log(action):
    with open(LOG_FILE, "a") as f:
        f.write(f"[{datetime.datetime.now()}] {action}\n")

# --- Built-in apps ---
def app_calculator():
    expr = input("Calc> ")
    try:
        print("Result:", eval(expr))
    except Exception as e:
        print("Error:", e)

def app_notes():
    note = input("Write a note: ")
    with open(DATA_FILE, "a") as f:
        f.write(note + "\n")
    print("Note saved!")

def app_game():
    target = random.randint(1, 10)
    guess = int(input("Guess 1-10: "))
    if guess == target:
        print("Correct!")
    else:
        print("Wrong, number was", target)

def app_calendar():
    print("Today's date:", datetime.date.today())

def app_todo():
    task = input("Add a todo task: ")
    with open(DATA_FILE, "a") as f:
        f.write(f"- {task}\n")
    print("Task added!")

# --- Apps dictionary ---
apps = {
    "calculator": app_calculator,
    "notes": app_notes,
    "game": app_game,
    "calendar": app_calendar,
    "todo": app_todo
}

# --- OS commands ---
def help_cmd():
    print("Commands: help, echo, clear, reboot, listapps, run <app>, version, settings, time, uptime")

def listapps():
    print("Installed apps:", ", ".join(apps.keys()))

def clear():
    print("\033[H\033[J", end="")

def reboot():
    print("Rebooting...")
    log("System rebooted")
    exit()

def version():
    print("AidanOS26.1 — Full Python OS in ONE file")
    log("Checked version")

START_TIME = time.time()
def uptime():
    print(f"Uptime: {int(time.time() - START_TIME)} seconds")
    log("Checked uptime")

def show_time():
    print("Current time:", datetime.datetime.now())
    log("Checked time")

# --- Update system ---
def check_updates():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(3)
        s.connect((UPDATE_SERVER, UPDATE_PORT))
        s.sendall(b"REQUEST_UPDATES\n")
        data = s.recv(65536).decode()
        if data:
            print("New update available. Update now? (Y/N)")
            choice = input("> ").upper()
            if choice == "Y":
                apply_update(data)
                print("Update applied. Rebooting...")
                reboot()
            else:
                print("Update skipped. You can update later in settings.")
        s.close()
    except Exception as e:
        print("No update server reachable:", e)

def apply_update(data):
    # In this single-file version, the server just replaces this file entirely
    filename = __file__
    with open(filename, "w") as f:
        f.write(data)
    log("Applied full OS update")

# --- Settings ---
def settings():
    print("1. Check for updates now")
    print("2. Show logs")
    print("3. Reboot")
    choice = input("Choice: ").strip()
    if choice == "1":
        check_updates()
    elif choice == "2":
        if os.path.exists(LOG_FILE):
            with open(LOG_FILE) as f:
                print(f.read())
        else:
            print("No logs yet.")
    elif choice == "3":
        reboot()

# --- Main shell ---
def main():
    print("Welcome to AidanOS26.1 (Single-File Python OS)")
    check_updates()
    while True:
        cmd = input("AidanOS> ").strip().split()
        if not cmd:
            continue
        if cmd[0] == "help":
            help_cmd()
        elif cmd[0] == "echo":
            print(" ".join(cmd[1:]))
        elif cmd[0] == "clear":
            clear()
        elif cmd[0] == "reboot":
            reboot()
        elif cmd[0] == "listapps":
            listapps()
        elif cmd[0] == "run" and len(cmd) > 1:
            if cmd[1] in apps:
                apps[cmd[1]]()
            else:
                print("App not found")
        elif cmd[0] == "version":
            version()
        elif cmd[0] == "settings":
            settings()
        elif cmd[0] == "time":
            show_time()
        elif cmd[0] == "uptime":
            uptime()
        else:
            print("Unknown command:", cmd[0])

if __name__ == "__main__":
    main()
<<END>>
