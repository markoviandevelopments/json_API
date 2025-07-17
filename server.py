import socket
import time
import random
import json

visit_count = 0

# Server configuration
HOST = '0.0.0.0'
PORT = 5090         # Port to listen on

# Create a TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)  # Listen for incoming connections (backlog of 1)

print(f"Server listening on {HOST}:{PORT}")

tribal_name = ["Walking Snake", "Running Tiger", "Singing Bear"]

while True:
    # Accept a client connection
    client_socket, addr = server_socket.accept()
    print(f"Connection from {addr}")
    
    # Generate data
    data = {
        "epoch_time": time.time(),
        "random_number": random.random(),
        "num visits": visit_count,
        "tribal name": random.choice(tribal_name)
    }
    
    # Convert to JSON
    json_data = json.dumps(data)
    
    # Send JSON data to client
    client_socket.sendall(json_data.encode('utf-8'))
    
    visit_count += 1

    # Close the client connection
    client_socket.close()
