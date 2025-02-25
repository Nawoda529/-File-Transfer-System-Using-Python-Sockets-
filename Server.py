import socket

# Define the host and port
host = '127.0.0.1'  # Localhost
port = 12345  # Port to bind the server

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a host and port
server_socket.bind((host, port))

# Listen for incoming connections (maximum of 1 connection)
server_socket.listen(1)
print(f"Server listening on {host}:{port}...")

# Accept a connection from a client
client_socket, client_address = server_socket.accept()
print(f"Connection established with {client_address}")

# Receive the filename from the client
filename = client_socket.recv(1024).decode()
print(f"Receiving file: {filename}")

# Open the file in write mode to save the received content
with open(filename, 'wb') as file:
    print("Saving the received file...")
    while True:
        # Receive data in chunks
        data = client_socket.recv(1024)
        if not data:
            break  # End of file
        file.write(data)

print("File received and saved successfully.")

# Close the connections
client_socket.close()
server_socket.close()
