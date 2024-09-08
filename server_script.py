import socket
import threading

SERVER_IP = socket.gethostbyname(socket.gethostname())
SERVER_PORT = 4242
ADDR = (SERVER_IP, SERVER_PORT)
FORMAT = "utf-8"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(connection, addr):
    print(f"[NOVA CONEXÃO] {addr} conectado.")

    connection.send(bytes("Bem-vindo ao servidor!", FORMAT))
    connection.close()

def start():
    server.listen()
    while True:
        clientSocket, address = server.accept()
        thread = threading.Thread(target=handle_client(clientSocket, address), args=(clientSocket, address))
        thread.start()

start()
