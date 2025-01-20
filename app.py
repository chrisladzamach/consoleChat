from server.server import start_server
from client.client import start_client

def main():
    print("Select mode:")
    print("1. Server")
    print("2. Client")
    option = input("Option: ")

    if option == '1':
        start_server()
    elif option == '2':
        start_client()
    else:
        print("[ERROR] Invalid option.")

if __name__ == "__main__":
    main()
