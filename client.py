import socket

SERVER = socket.gethostbyname(socket.gethostname())
PORT = 4040

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((SERVER, PORT))

def send(msg):
    messages = msg.encode('utf-8')
    msg_length = len(messages)
    send_length = str(msg_length).encode('utf-8')
    send_length += b' ' * (64 - len(send_length))
    client.send(send_length)
    client.send(messages)
    msg_server = client.recv(1024).decode('utf-8')
    print(msg_server)

send("Hello World")
send("!DISCONNECT")

