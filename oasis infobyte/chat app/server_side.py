import socket
import threading

def handle_client(client_socket, client_address):
    print(f"Connected with {client_address}")

    while True:
        message = client_socket.recv(1024).decode("utf-8")
        if message.lower() == "exit":
            break
        print(f"Received from {client_address}: {message}")

    print(f"Disconnected from {client_address}")
    client_socket.close()

def start_server(host, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"Server listening on {host}:{port}")

    while True:
        client_socket, client_address = server_socket.accept()
        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_thread.start()

if __name__ == "__main__":
    HOST = '127.0.0.1'  # localhost
    PORT = 12345  # Choose any available port

    start_server(HOST, PORT)
