import socket
import threading
from server.handler import handle_client
from utils.config import HOST, PORT

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(5)

    print(f"[SERVER] Waiting for connections on {HOST}:{PORT}")

    clients = []
    nicknames = {}

    while True:
        client, address = server.accept()
        clients.append(client)
        print(f"[NEW CLIENT] Connected from {address}")

        thread = threading.Thread(target=handle_client, args=(client, address, clients, nicknames))
        thread.start()
