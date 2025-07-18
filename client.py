import socket
import json
import types

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
parsed_data = types.SimpleNamespace(**parsed_data)

# Print the received data
print("Received JSON:")
print(parsed_data)
print(f"Random Number: {parsed_data.random_number}")
print(f"Dictionary: {parsed_data.__dict__}")

# Close the socket
client_socket.close()
