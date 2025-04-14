import socket
HOST = '127.0.0.1'
PORT = 4950
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))
print("Connected to the server. Type 'quit' to exit.")
while True:
    message = input("You: ")
    client_socket.send(message.encode())
    if message.lower() == 'quit':
        break
    response = client_socket.recv(1024).decode()
    print(f"Server: {response}")
client_socket.close()