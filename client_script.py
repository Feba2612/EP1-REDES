import socket
import inquirer
import typer

PORT = 4242
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

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
    pass