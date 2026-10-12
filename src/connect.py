import socket 
from rich import print

def tryConnection(port, target_ip):
    if isinstance(port, int):
        port = [port]   
    for p in port:
        scan = (target_ip, p)
        # O AF_INET é usado para identificar o IPv4 e o SOCK_STREAM o TCP
        connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1.0)   # Essa função define o limite de tempo para a conexão

        result = connection.connect_ex(scan)
        if result == 0:
            print(f"[green]Port {p} - Open[/]")
        connection.close()    # Essa função é usada para encerrar a conexão e finalizar o processo

