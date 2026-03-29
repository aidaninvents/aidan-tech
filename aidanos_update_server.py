# aidanos_update_server.py
# Python Update Server for AidanOS26 clients

import socket, os

HOST = '0.0.0.0'  # Listen on all interfaces
PORT = 12345      # Must match client UPDATE_PORT

# Folder to store update files
UPDATE_FOLDER = "aidanos_update_files"
os.makedirs(UPDATE_FOLDER, exist_ok=True)

def get_update_data():
    """
    Reads all .py files in UPDATE_FOLDER and formats them
    for the client: filename\ncontent\n<<END>>
    """
    data = ""
    for filename in os.listdir(UPDATE_FOLDER):
        if filename.endswith(".py"):
            with open(os.path.join(UPDATE_FOLDER, filename)) as f:
                content = f.read()
            data += f"{filename}\n{content}\n<<END>>\n"
    return data

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"AidanOS Update Server running on port {PORT}")
    print(f"Place Python files (.py) in '{UPDATE_FOLDER}' folder to serve as updates.")
    while True:
        conn, addr = s.accept()
        with conn:
            print(f"Client connected: {addr}")
            try:
                data = conn.recv(1024).decode().strip()
                if data == "REQUEST_UPDATES":
                    updates = get_update_data()
                    if updates:
                        conn.sendall(updates.encode())
                    else:
                        conn.sendall(b"")  # no updates
                else:
                    conn.sendall(b"INVALID_REQUEST")
            except Exception as e:
                print(f"Error with client {addr}: {e}")