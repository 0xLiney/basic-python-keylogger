Basic Python Keylogger
This project provides a simple Python-based keylogger with both client and server components, designed strictly for educational purposes.

Installation
Clone the Repository:

   
   git clone https://github.com/LineyGH/basic-python-keylogger.git
   


Navigate to the Project Directory:

   
   cd basic-python-keylogger
   


Install Required Dependencies:

   Ensure you have Python installed. The keylogger utilizes the pynput library for capturing keyboard inputs. Install it using:

   
   pip install pynput
   


Usage
Run the Server:

   The server script listens for incoming connections and logs keystrokes sent by the client.

   
   python server.py
   


   This will create a KeyLog.txt file in the same directory to store captured keystrokes.

Configure the Client:

   Before running the client script, update the server IP address in client.py to match your server's IP.

   
   # Inside clientside.py
   SERVER_IP = 'your_server_ip_here'
   


Run the Client:

   The client script captures keystrokes and sends them to the server.

   
   python client.py
   


Implementation Details
Server Side:
Compatible with multiple operating systems (Windows, macOS, Linux).
Captures all incoming keystrokes and stores them in KeyLog.txt.
Displays the connected client's IP address.

Client Side:
Compatible with multiple operating systems.
Establishes a connection with the server and transmits captured keystrokes.

Disclaimer
This keylogger is intended solely for educational purposes. Unauthorized use on systems without explicit consent is illegal and unethical. The author is not responsible for any misuse of this tool. 
