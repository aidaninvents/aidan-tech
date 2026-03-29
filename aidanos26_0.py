# AidanOS26.0 Full Python OS
# Save as aidanos26_0_full.py

import os, datetime, socket, time

# --- Setup folders ---
os.makedirs("aidanos_notes", exist_ok=True)
os.makedirs("aidanos_todo", exist_ok=True)
os.makedirs("aidanos_apps", exist_ok=True)
LOG_FILE = "logs.txt"

# --- Logging function ---
def log(action):
    with open(LOG_FILE, "a") as f:
        f.write(f"[{datetime.datetime.now()}] {action}\n")

# --- Apps ---
def calculator():
    try:
        expr = input("Calc> ")
        print("Result:", eval(expr))
        log(f"Used calculator: {expr}")
    except Exception as e:
        print("Error:", e)

def notes():
    note = input("Write a note: ")
    with open("aidanos_notes/notes.txt", "a") as f:
        f.write(f"[{datetime.datetime.now()}] {note}\n")
    print("Note saved!")
    log(f"Wrote note: {note}")

def game():
    target = 5  # Simple number guessing game
    guess = int(input("Guess 1-10: "))
    if guess == target:
        print("Correct!")
    else:
        print("Wrong, number was", target)
    log(f"Played game, guessed {guess}")

def calendar():
    print("Today's date:", datetime.date.today())
    log("Checked calendar")

def todo():
    task = input("Add a todo task: ")
    with open("aidanos_todo/tasks.txt", "a") as f:
        f.write(f"- {task}\n")
    print("Task added!")
    log(f"Added todo: {task}")

apps = {
    "calculator": calculator,
    "notes": notes,
    "game": game,
    "calendar": calendar,
    "todo": todo
}

# --- OS Commands ---
def help_cmd():
    print("Commands: help, echo, clear, reboot, listapps, run <app>, version, settings")

def listapps():
    print("Installed apps:", ", ".join(apps.keys()))

def run_app(name):
    if name in apps:
        apps[name]()
    else:
        print("App not found:", name)

def clear():
    print("\033[H\033[J", end="")

def reboot():
    print("Rebooting...")
    log("Rebooted system")
    exit()

def version():
    print("AidanOS26.0 — Full Python OS with updates & file uploads")
    log("Checked version")

# --- Update system ---
UPDATE_SERVER = "127.0.0.1"  # change to server IP
UPDATE_PORT = 12345

def check_updates():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(3)
        s.connect((UPDATE_SERVER, UPDATE_PORT))
        s.sendall(b"REQUEST_UPDATES\n")
        data = s.recv(4096).decode()
        if data:
            print("New update available. Do you want to update? (Y/N)")
            choice = input("AidanOS> ").strip().upper()
            if choice == "Y":
                log("Update accepted")
                apply_updates(data)
                print("Update applied. Rebooting...")
                reboot()
            else:
                print("Update skipped. You can manually update in settings.")
                log("Update declined")
        s.close()
    except Exception as e:
        print("No update server reachable.")
        log(f"Update check failed: {e}")

def apply_updates(data):
    # data format: filename\ncontent\n<<END>>
    entries = data.split("<<END>>")
    for entry in entries:
        if entry.strip() == "":
            continue
        try:
            filename, content = entry.strip().split("\n", 1)
            with open(f"aidanos_apps/{filename}", "w") as f:
                f.write(content)
            print(f"Updated: {filename}")
            log(f"Updated file: {filename}")
        except:
            continue

# --- Settings command ---
def settings():
    print("Settings Menu:")
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

# --- Main Shell ---
def main():
    print("Welcome to AidanOS26.0 — Full Python OS with Updates & Uploads")
    check_updates()  # auto-check at startup
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
            run_app(cmd[1])
        elif cmd[0] == "version":
            version()
        elif cmd[0] == "settings":
            settings()
        else:
            print("Unknown command:", cmd[0])

if __name__ == "__main__":
    main()