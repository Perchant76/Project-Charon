import socket
import threading
import time
# Connection Data
print("""
 ▄████▄   ██░ ██  ▄▄▄      ██▀███   ▒█████   ███▄    █       ██████  ▓█████ ██▀███   ██▒   █▓ ▓█████ ██▀███  
▒██▀ ▀█ ▒▓██░ ██ ▒████▄   ▓██ ▒ ██▒▒██▒  ██▒ ██ ▀█   █     ▒██    ▒  ▓█   ▀▓██ ▒ ██▒▓██░   █▒ ▓█   ▀▓██ ▒ ██▒
▒▓█    ▄░▒██▀▀██ ▒██  ▀█▄ ▓██ ░▄█ ▒▒██░  ██▒▓██  ▀█ ██▒    ░ ▓██▄    ▒███  ▓██ ░▄█ ▒ ▓██  █▒░ ▒███  ▓██ ░▄█ ▒
▒▓▓▄ ▄██ ░▓█ ░██ ░██▄▄▄▄██▒██▀▀█▄  ▒██   ██░▓██▒  ▐▌██▒      ▒   ██▒ ▒▓█  ▄▒██▀▀█▄    ▒██ █░░ ▒▓█  ▄▒██▀▀█▄  
▒ ▓███▀  ░▓█▒░██▓▒▓█   ▓██░██▓ ▒██▒░ ████▓▒░▒██░   ▓██░    ▒██████▒▒▒░▒████░██▓ ▒██▒   ▒▀█░  ▒░▒████░██▓ ▒██▒
░ ░▒ ▒    ▒ ░░▒░▒░▒▒   ▓▒█░ ▒▓ ░▒▓░░ ▒░▒░▒░ ░ ▒░   ▒ ▒     ▒ ▒▓▒ ▒ ░░░░ ▒░ ░ ▒▓ ░▒▓░   ░ ▐░  ░░░ ▒░ ░ ▒▓ ░▒▓░
  ░  ▒    ▒ ░▒░ ░░ ░   ▒▒   ░▒ ░ ▒   ░ ▒ ▒░ ░ ░░   ░ ▒░    ░ ░▒  ░ ░░ ░ ░    ░▒ ░ ▒    ░ ░░  ░ ░ ░    ░▒ ░ ▒ 
░         ░  ░░ ░  ░   ▒    ░░   ░ ░ ░ ░ ▒     ░   ░ ░     ░  ░  ░      ░    ░░   ░       ░      ░    ░░   ░ 
░ ░       ░  ░  ░      ░     ░         ░ ░           ░           ░  ░   ░     ░           ░  ░   ░     ░     
made by Perchant76
""")
host = '127.0.0.1'
port = 55555
textfile = open("log.txt", "w")
# Starting Server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

# Lists For Clients and Their Nicknames
clients = []
nicknames = []
# Sending Messages To All Connected Clients
def broadcast(message):
    for client in clients:
        client.send(message)
        
# Handling Messages From Clients
def handle(client):
    while True:
        try:
            # Broadcasting Messages
            message = client.recv(1024)
            broadcast(message)
        except:
            # Removing And Closing Clients
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast('{} left!'.format(nickname).encode('ascii'))
            nicknames.remove(nickname)
            break
# Receiving / Listening Function
def receive():
    while True:
        # Accept Connection
        client, address = server.accept()
        print("Connected with {}".format(str(address)))

        # Request And Store Nickname
        client.send('NICK'.encode('ascii'))
        nickname = client.recv(1024).decode('ascii')
        nicknames.append(nickname)
        clients.append(client)

        # Print And Broadcast Nickname
        print("Nickname is {}".format(nickname))
        broadcast(f"{nickname} joined!".encode('ascii'))
        client.send('Connected to server!'.encode('ascii'))

        # Start Handling Thread For Client
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()
print("server is running...")
receive()
time.sleep(10)
