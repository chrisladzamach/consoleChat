import socket
import threading
from utils.config import PORT

def start_client():
    server_ip = input("Enter server IP: ")

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((server_ip, PORT))

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
