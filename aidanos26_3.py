# AidanOS26.3 Super — Full Python OS in ONE file

import os, time, datetime, socket, random

# --- Configuration ---
UPDATE_SERVER = "127.0.0.1"  # Fake server
UPDATE_PORT = 12345
LOG_FILE = "logs_super.txt"
DATA_FILE = "data_super.txt"

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
    log(f"Calculator used: {expr}")

def app_notes():
    note = input("Write a note: ")
    with open(DATA_FILE, "a") as f:
        f.write(note + "\n")
    print("Note saved!")
    log("Note added")

def app_game():
    target = random.randint(1, 10)
    guess = int(input("Guess 1-10: "))
    if guess == target:
        print("Correct!")
        log(f"Game won with guess {guess}")
    else:
        print("Wrong, number was", target)
        log(f"Game lost with guess {guess}")

def app_calendar():
    today = datetime.date.today()
    print("Today's date:", today)
    log("Calendar opened")

def app_todo():
    task = input("Add a todo task: ")
    with open(DATA_FILE, "a") as f:
        f.write(f"- {task}\n")
    print("Task added!")
    log(f"Todo added: {task}")

def app_weather():
    temp = random.randint(50, 100)
    print(f"Weather forecast: {temp}°F, sunny")
    log("Weather checked")

def app_dice():
    sides = int(input("Number of sides on dice: "))
    roll = random.randint(1, sides)
    print(f"Rolled: {roll}")
    log(f"Dice rolled: {roll}/{sides}")

def app_editor():
    print("Mini text editor (type 'SAVE' to finish)")
    content = []
    while True:
        line = input()
        if line.strip().upper() == "SAVE":
            break
        content.append(line)
    with open(DATA_FILE, "a") as f:
        f.write("\n".join(content)+"\n")
    print("File saved!")
    log("Editor used and saved content")

# --- Apps dictionary ---
apps = {
    "calculator": app_calculator,
    "notes": app_notes,
    "game": app_game,
    "calendar": app_calendar,
    "todo": app_todo,
    "weather": app_weather,
    "dice": app_dice,
    "editor": app_editor
}

# --- OS commands ---
def help_cmd():
    print("Commands: help, echo, clear, reboot, shutdown, listapps, run <app>, version, settings, time, uptime, joke, info")

def listapps():
    print("Installed apps:", ", ".join(apps.keys()))

def clear():
    print("\033[H\033[J", end="")

def reboot():
    print("Rebooting...")
    log("System rebooted")
    exit()

def shutdown():
    print("Shutting down...")
    log("System shutdown")
    exit()

def version():
    print("AidanOS26.3 Super — Full Python OS in ONE file")
    log("Checked version")

START_TIME = time.time()
def uptime():
    print(f"Uptime: {int(time.time() - START_TIME)} seconds")
    log("Checked uptime")

def show_time():
    now = datetime.datetime.now()
    print("Current time:", now)
    log("Checked time")

def joke():
    jokes = ["Why did the Python cross the road? To import the other side!",
             "Debugging: Removing the needles from the haystack!",
             "There are 10 types of people: those who understand binary..."]
    print(random.choice(jokes))
    log("Told a joke")

def info():
    print("AidanOS26.3 Super — Advanced Python OS with extra apps!")
    log("Checked system info")

# --- Update system ---
def check_updates():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(3)
        s.connect((UPDATE_SERVER, UPDATE_PORT))
        s.sendall(b"REQUEST_SUPER_UPDATES\n")
        data = s.recv(65536).decode()
        if data:
            print("Super update available. Apply? (Y/N)")
            choice = input("> ").upper()
            if choice == "Y":
                apply_update(data)
                print("Super update applied. Rebooting...")
                reboot()
            else:
                print("Update skipped. Can be applied later.")
        s.close()
    except Exception as e:
        print("No update server reachable:", e)

def apply_update(data):
    filename = __file__
    with open(filename, "w") as f:
        f.write(data)
    log("Applied super OS update")

# --- Settings ---
def settings():
    print("1. Check for super updates")
    print("2. Show logs")
    print("3. Reboot")
    print("4. Shutdown")
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
    elif choice == "4":
        shutdown()

# --- Main shell ---
def main():
    print("Welcome to AidanOS26.3 Super (Single-File Python OS)")
    check_updates()
    while True:
        cmd = input("AidanOS> ").strip().split()
        if not cmd:
            continue
        action = cmd[0].lower()
        if action == "help":
            help_cmd()
        elif action == "echo":
            print(" ".join(cmd[1:]))
        elif action == "clear":
            clear()
        elif action == "reboot":
            reboot()
        elif action == "shutdown":
            shutdown()
        elif action == "listapps":
            listapps()
        elif action == "run" and len(cmd) > 1:
            app_name = cmd[1].lower()
            if app_name in apps:
                apps[app_name]()
            else:
                print("App not found")
        elif action == "version":
            version()
        elif action == "settings":
            settings()
        elif action == "time":
            show_time()
        elif action == "uptime":
            uptime()
        elif action == "joke":
            joke()
        elif action == "info":
            info()
        else:
            print("Unknown command:", action)

if __name__ == "__main__":
    main()