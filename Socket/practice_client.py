# This program is the opposite of basic_client.py, whereby it sends data to practice_server.py
import socket

my_socket = socket.socket()

address = input('Enter IPv4 address of server: ')
port = int(input('Enter Port number of server: '))

my_socket.connect((address, port))
my_socket.sendall(b'Hello from client\n')
my_socket.close()