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

    cliente.send(
        f"pokemons_escolhidos|{pokemons_escolhidos['pokemons']}".encode("utf-8"))


if __name__ == "__main__":
    try:
        cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        cliente.connect(ADDR)
    except Exception as e:
        typer.echo(f"Erro ao conectar ao servidor: {e}")
        exit()

    typer.echo("Bem vindo à batalha Pokémon!")

    nome = typer.prompt("Digite seu nome: ")
    cliente.send(f"nome|{nome}".encode("utf-8"))
    print("Conectado ao servidor!")

    while True:
        escolher_pokemons(cliente)
        break
