import socket 
import threading
from server.handler import handle_client
from utils.config import HOST, PORT
from colorama import init, Fore, Back, Style

init()
def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(5)

    print(Fore.RED + f"[SERVER] Waiting for connections on {HOST}:{PORT}" + Fore.RESET)

    clients = []
    nicknames = {}
    
    def accept_clients():
        while True:
            try:
                client, address = server.accept()
                clients.append(client)
                print(Fore.GREEN + f"{client} Connected from {address}" + Fore.RESET)
                thread = threading.Thread(target=handle_client, args=(client, address, clients, nicknames))
                thread.start()
            except OSError:
                break
    
    accept_thread = threading.Thread(target=accept_clients)
    accept_thread.start()
    
    while True:
        command = input()
        if command.lower() == "exit":
            print(Fore.RED + "[SERVER] Shutting down..." + Fore.RESET)
            server.close()
            break
