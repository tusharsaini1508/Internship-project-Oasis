import socket
import threading

def send_message(client_socket):
    while True:
        message = input("Enter message: ")
        client_socket.send(message.encode("utf-8"))
        if message.lower() == "exit":
            break

def start_client(host, port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    print(f"Connected to server on {host}:{port}")

    send_thread = threading.Thread(target=send_message, args=(client_socket,))
    send_thread.start()

    while True:
        message = client_socket.recv(1024).decode("utf-8")
        if message.lower() == "exit":
            print("Server closed the connection.")
            break
        print(f"Received from server: {message}")

    client_socket.close()

if __name__ == "__main__":
    HOST = '127.0.0.1'  # localhost
    PORT = 12345  # Same port used by the server

    start_client(HOST, PORT)
