from colorama import init, Fore, Back, Style
import socket
import threading
from utils.config import PORT

init()
def start_client():
    server_ip = input("Enter server IP: ")

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((server_ip, PORT))

    nickname = input(Fore.BLUE + "Enter your nickname: " + Fore.RESET)
    client.send(nickname.encode('utf-8'))

    def receive_messages():
        while True:
            try:
                message = client.recv(1024).decode('utf-8')
                print(message)
            except:
                print(Fore.RED + "[ERROR] Connection lost." + Fore.RESET)
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
