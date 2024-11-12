Basic Python Keylogger (Client and Server Sides)
Overview
This project consists of a basic keylogger implemented in Python, featuring both client and server components. The server-side script listens for incoming connections and logs keystrokes sent by the client-side script.

Note: This project is for educational purposes only. The author is not responsible for any malicious or illegal use of this tool. Use responsibly and with documented permission.

Features
Server Side
Compatibility: Works on multiple devices (Windows, Mac, Linux, etc.).
Functionality:
Captures all incoming keystrokes.
Stores captured keystrokes in a KeyLog.txt file located in the same directory.
Displays connected IP addresses.
Client Side
Compatibility: Works on multiple devices (Windows, Mac, Linux, etc.).
Functionality:
Establishes a connection with the server.
Sends all captured keystrokes to the server, where they are stored.
Important:
Ensure the server IP address is updated in the client script before use to establish a connection.
Usage
Run the server-side script to start listening for connections.
Run the client-side script on the target machine to initiate a connection and begin capturing keystrokes.
Disclaimer
STRICTLY FOR EDUCATIONAL PURPOSE ONLY.
I do not take responsibility for any malicious or illegal use of this tool. I do not condone the use of this keylogger for illicit activities unless proper permission has been provided and documented.


Installation
Clone the repository:
bash
Copy code
git clone https://github.com/LineyGH/basic-python-keylogger.git
Navigate to the project directory:
bash
Copy code
cd your-repo
Run the server script:
bash
Copy code
python3 server.py
Modify the client script with the server IP address and run:
bash
Copy code
python3 client.py


Contributing
Contributions are welcome! Please open an issue or submit a pull request for improvements or features.

Feel free to edit or replace the placeholder content with your own!
