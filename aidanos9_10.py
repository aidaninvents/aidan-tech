import os, datetime, socket, time

print('Welcome to AidanOS9.10 — Full Python OS shell')

# --- Setup folders ---
os.makedirs('aidanos_notes', exist_ok=True)
os.makedirs('aidanos_todo', exist_ok=True)
os.makedirs('aidanos_apps', exist_ok=True)

LOG_FILE = 'logs.txt'
def log(action):
    with open(LOG_FILE,'a') as f:
        f.write(f"[{datetime.datetime.now()}] {action}\n")

def calculator():
    try:
        expr = input('Calc> ')
        print('Result:', eval(expr))
        log(f'Used calculator: {expr}')
    except Exception as e:
        print('Error:', e)

def notes():
    note = input('Write a note: ')
    with open('aidanos_notes/notes.txt','a') as f:
        f.write(f"[{datetime.datetime.now()}] {note}\n")
    print('Note saved!')
    log(f'Wrote note: {note}')

def game():
    target = 5
    guess = int(input('Guess 1-10: '))
    if guess==target:
        print('Correct!')
    else:
        print('Wrong, number was', target)
    log(f'Played game, guessed {guess}')

def main():
    print('Starting AidanOS9.10 shell...')
    while True:
        cmd = input('AidanOS9.10> ').strip().split()
        if not cmd: continue
        if cmd[0]=='exit': break
        elif cmd[0]=='calc': calculator()
        elif cmd[0]=='notes': notes()
        else: print('Unknown command:', cmd[0])

if __name__=='__main__':
    main()
