import socket
HOST = '127.0.0.1'
PORT = 4950
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)
print(f"Server listening on {HOST}:{PORT}...")
client_socket, client_address = server_socket.accept()
print(f"New connection from {client_address}")
while True:
    data = client_socket.recv(1024).decode()
    if not data or data.lower() == 'quit':
        print("Client disconnected.")
        break
    print(f"Client: {data}")
    reply = input("Reply: ")
    client_socket.send(reply.encode())
client_socket.close()
server_socket.close()