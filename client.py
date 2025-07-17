import socket
import json

# Server configuration (must match the server's HOST and PORT)
HOST = '192.168.1.126'
PORT = 5090

# Create a TCP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((HOST, PORT))

# Receive data from the server (assuming JSON is not too large)
data = client_socket.recv(1024)  # Buffer size of 1024 bytes

# Decode and parse JSON
json_data = data.decode('utf-8')
parsed_data = json.loads(json_data)

# Print the received data
print("Received JSON:")
print(parsed_data)

# Close the socket
client_socket.close()
