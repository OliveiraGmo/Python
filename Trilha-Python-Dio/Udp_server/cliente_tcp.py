import socket
import sys

def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except socket.error as e:
        print("A conexão falhou")
        print(f'Erro: {e}')
        sys.exit()
    print("Soket criado com sucesso")

    HostAlvo = input(("Digite o Host ou ip a ser conectafo: "))
    PortaAlvo = input("Digite a porta a ser conectada: ")

    try:
        s.connect((HostAlvo, int(PortaAlvo)))
        print(f"Cliente TCP conectado com sucesso no host: {HostAlvo} e na porta :{PortaAlvo}")
        s.shutdown(2)
    except socket.error as e:
        print((f"Erro {e}"))
if __name__== "__main__":
    main()