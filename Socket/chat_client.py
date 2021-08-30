# Program 7
# import socket
#
# chat_socket = socket.socket()
#
# address = input('Enter IPv4 address of server: ')
# port = int(input('Enter Port number of server: '))
#
# chat_socket.connect((address, port))
# while True:
#     print('WAITING FOR SERVER...')
#     data = b''
#     while b'\n' not in data:
#         data += chat_socket.recv(1024)
#     print('SERVER WROTE: ' + data.decode())
#     data = input('CLIENT INPUT: ').encode()
#     chat_socket.sendall(data + b'\n')

# modified chat_client
import socket

chat_socket = socket.socket()

address = input('Enter IPv4 address of server: ')
port = int(input('Enter Port number of server: '))

chat_socket.connect((address, port))
while True:
    print('WAITING FOR SERVER...')
    data = b''
    while b'\n' not in data:
        data += chat_socket.recv(1024)
    if b'quit' in data:
        print("SERVER DISCONNECTED...")
        chat_socket.close()
        break
    print('SERVER WROTE: ' + data.decode())
    data = input('CLIENT INPUT: ').encode()
    chat_socket.sendall(data + b'\n')
    if b'quit' in data:
        chat_socket.close()
        break