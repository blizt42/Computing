# Program 4
import socket

my_socket = socket.socket()

address = input('Enter IPv4 address of server: ')
port = int(input('Enter Port number of server: '))

my_socket.connect((address, port))
data = b''
while b'\n' not in data:
    data += my_socket.recv(1024)
print(data)
my_socket.close()
