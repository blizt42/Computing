# Program 1
import socket

my_socket = socket.socket()                  # Creates a class object of a socket
my_socket.bind(('127.0.0.1', 29126))         # binds the class object to a specific address and port
my_socket.listen()                           # waits and listen for any incoming connections

new_socket, addr = my_socket.accept()        # accepts and incoming connection
print('Connected to ' + str(addr))
new_socket.sendall(b'Hello from server\n')   # Sends an message in bytes
new_socket.close()
my_socket.close()