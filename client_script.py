import socket
import threading

PORT = 4242
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

msg = client.recv(1024).decode()

print(msg)