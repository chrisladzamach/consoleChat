import socket
import threading

def server():
    host = '0.0.0.0'
    port = 5555

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(5)

    print(f"[SERVER] Waiting for connections on {host}:{port}")

    clients = []
    nicknames = {}
    
    def handle_client(client, address):
        print(f"[NEW CLIENT] Connected from {address}")
        
        nickname = client.recv(1024).decode('utf-8')
        nicknames[client] = nickname

        while True:
            try:
                message = client.recv(1024).decode('utf-8')
                if message:
                    print(f"[{nicknames[client]}] {message}")

                    for c in clients:
                        if c != client:
                            c.send(f"[{nicknames[client]}] {message}".encode('utf-8'))
                else:
                    break
            except:
                break

        print(f"[DISCONNECTED] {address}")
        clients.remove(client)
        del nicknames[client]
        client.close()

    while True:
        client, address = server.accept()
        clients.append(client)
        thread = threading.Thread(target=handle_client, args=(client, address))
        thread.start()

def client():
    server_ip = input("Enter server IP: ")
    port = 5555

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((server_ip, port))

    nickname = input("Enter your nickname: ")
    client.send(nickname.encode('utf-8'))

    def receive_messages():
        while True:
            try:
                message = client.recv(1024).decode('utf-8')
                print(message)
            except:
                print("[ERROR] Connection lost.")
                client.close()
                break

    thread = threading.Thread(target=receive_messages)
    thread.start()

    while True:
        message = input("Msg: ")
        if message.lower() == 'exit':
            client.close()
            break
        client.send(message.encode('utf-8'))


if __name__ == "__main__":
    print("Select mode:")
    print("1. Server")
    print("2. Client")
    option = input("Option: ")

    if option == '1':
        server()
    elif option == '2':
        client()
    else:
        print("[ERROR] Invalid option.")