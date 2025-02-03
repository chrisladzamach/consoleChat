from colorama import init, Fore, Back, Style
init()

def handle_client(client, address, clients, nicknames):
    try:
        nickname = client.recv(1024).decode('utf-8')
        nicknames[client] = nickname
        print(Fore.GREEN + f"{nickname} connected from {address}" + Fore.RESET)

        while True:
            try:
                message = client.recv(1024).decode('utf-8')
                if message:
                    print(f"[{nickname}] {message}")

                    for c in clients:
                        if c != client:
                            c.send(f"[{nickname}] {message}".encode('utf-8'))
                else:
                    break
            except:
                break
    finally:
        print(Fore.RED + f"[DISCONNECTED] {address}" + Fore.RESET)
        clients.remove(client)
        del nicknames[client]
        client.close()
