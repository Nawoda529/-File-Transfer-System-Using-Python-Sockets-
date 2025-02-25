import socket

# Define the server's host and port
host = '127.0.0.1'  # Localhost
port = 12345  # Port to connect to the server

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((host, port))

# Specify the file you want to send
filename = 'testfile.txt'

# Send the filename to the server
client_socket.send(filename.encode())

# Open the file to send
with open(filename, 'rb') as file:
    print("Sending file...")
    while True:
        # Read the file in chunks of 1024 bytes
        data = file.read(1024)
        if not data:
            break  # End of file
        client_socket.send(data)

print("File sent successfully.")

# Close the connection
client_socket.close()
