import socket
import threading

SERVER = socket.gethostbyname(socket.gethostname())
PORT = 4040

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((SERVER, PORT))

def handle_client(conn, addr):
    print(f"Connect by {addr}")
    connection = True
    while connection:
        msg_length = conn.recv(64).decode('utf-8')
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode('utf-8')
            if msg == "!DISCONNECT":
                connection = False
            print(f"{addr} messages = {msg}")
            conn.send("Thank you for communicate to server!".encode('utf-8'))
    conn.close()
        

def start():
    s.listen()
    while True:
        conn, addr = s.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"Connection new {threading.active_count() - 1}")

print("SERVER READY")
start()