import os
from server.server import start_server
from client.client import start_client
from colorama import init, Fore

init()

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    while True:
        clear_console()
        print("Select mode:")
        print("1. Server")
        print("2. Client")
        option = input("Option: ")

        if option == '1':
            start_server()
            break
        elif option == '2':
            start_client()
            break
        else:
            clear_console()
            print(Fore.RED + "[ERROR] Invalid option. Please try again." + Fore.RESET)

if __name__ == "__main__":
    main()
