import socket
import inquirer
import typer
from inquirer.themes import BlueComposure

PORT = 4242
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

def escolher_pokemons(cliente):
    pokemons = [
        inquirer.Checkbox("pokemons", message="Escolha seus pokémons (max 2)", choices=[
            "Charmander", "Bulbasaur", "Squirtle", "Pikachu"
        ], default=[])
    ]

    pokemons_escolhidos = inquirer.prompt(pokemons, theme=BlueComposure())
    pokemons_str = ','.join(pokemons_escolhidos['pokemons'])
    cliente.send(f"pokemons_escolhidos|{pokemons_str}".encode("utf-8"))

    resposta = cliente.recv(1024).decode("utf-8")
    print(resposta)  # Exibe resposta do servidor sobre os pokémons

def escolher_acao(cliente):
    acoes = [
        inquirer.List("acao", message="O que será feito?", choices=[
            "Atacar", "Itens", "Fugir"
        ], default="Atacar")
    ]

    acao_escolhida = inquirer.prompt(acoes, theme=BlueComposure())
    cliente.send(f"acao_escolhida|{acao_escolhida['acao']}".encode("utf-8"))

    resposta = cliente.recv(1024).decode("utf-8")
    print(resposta)  # Exibe resposta do servidor sobre a ação

if __name__ == "__main__":
    try:
        cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        cliente.connect(ADDR)
    except Exception as e:
        typer.echo(f"Erro ao conectar ao servidor: {e}")
        exit()

    typer.echo("Bem-vindo à batalha Pokémon!")

    nome = typer.prompt("Digite seu nome: ")
    cliente.send(f"nome|{nome}".encode("utf-8"))
    print("Conectado ao servidor!")

    while True:
        escolher_pokemons(cliente)
        escolher_acao(cliente)
        # Recebe uma mensagem de "próximo turno" ou "pronto para próximo jogador" se necessário
        cliente.recv(1024)  # Aqui você pode aguardar uma confirmação do servidor
