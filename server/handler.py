def handle_client(client, address, clients, nicknames):
    try:
        nickname = client.recv(1024).decode('utf-8')
        nicknames[client] = nickname
        print(f"[NICKNAME SET] {nickname} connected from {address}")

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
        print(f"[DISCONNECTED] {address}")
        clients.remove(client)
        del nicknames[client]
        client.close()
