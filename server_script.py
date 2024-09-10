import socket
import threading

SERVER_IP = socket.gethostbyname(socket.gethostname())
SERVER_PORT = 4242
ADDR = (SERVER_IP, SERVER_PORT)
FORMAT = "utf-8"

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind(ADDR)


class Jogador:
    def __init__(self, socket):
        self.nome = None
        self.socket = socket
        self.socket_adversario = None

    def set_nome(self, nome):
        self.nome = nome


def get_jogador_info(jogador):
    nome_msg = jogador.socket.recv(1024).decode(FORMAT)
    nome = nome_msg.split("|")[1]
    jogador.set_nome(nome)
    print(f"Jogador conectado: {jogador.nome}")

    pass


def main():
    servidor.listen(2)
    print(f"Servidor rodando em {SERVER_IP}:{SERVER_PORT}")
    num_conexoes = 0
    while True:
        socket_cliente = servidor.accept()
        num_conexoes += 1

        if num_conexoes == 1:
            jogador1 = Jogador(socket_cliente)
            jogador1_thread = threading.Thread(target=get_jogador_info(
                jogador1), args=(jogador1, socket_cliente))
            jogador1_thread.start()
        else:
            jogador2 = Jogador(socket_cliente)
            jogador2_thread = threading.Thread(target=get_jogador_info(
                jogador2), args=(jogador2, socket_cliente))
            jogador2_thread.start()


if __name__ == "__main__":
    print("[INICIANDO] Servidor está iniciando...")
    main()
