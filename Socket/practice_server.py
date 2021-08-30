# This program is the opposite of basic_server.py, whereby it receives data from practice_client.py
import socket

my_socket = socket.socket()
my_socket.bind(('127.0.0.1', 29126))
my_socket.listen()

new_socket, addr = my_socket.accept()
print(new_socket.recv(1024))
new_socket.close()
my_socket.close()