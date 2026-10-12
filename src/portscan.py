import argparse
from connect import tryConnection
from rich import print

parser = argparse.ArgumentParser(prog="Portscan", description="Ferramenta desenvolvida em Python para analisar possíveis portas abertas")
parser.add_argument('target_ip', help='O IP do alvo a ser feita o scan')
parser.add_argument("-a", "--all", action="store_true", help="Flag para fazer o scan em todas as portas")
parser.add_argument("-p", "--ports", help="Portas a serem analisadas, separadas por vírgula")
args = parser.parse_args()
portClosed = 0

if args.all is True:
    for port in range(1, 65536):
        tryConnection(port, args.target_ip)
        if tryConnection is False:
            portClosed += 1
    print(f"[red]Portas fechadas: {portClosed}[/]")

elif args.ports is not None:
    ports = args.ports.split(',')
    for port in ports:
        port = int(port)
        tryConnection(port, args.target_ip)

else:
    print("Comando inválido. Use -h para ajuda.")
