# Program 6
# import socket
#
# listen_socket = socket.socket()
# listen_socket.bind(('127.0.0.1', 29126))
# listen_socket.listen()
#
# chat_socket, addr = listen_socket.accept()
# while True:
#     data = input('INPUT SERVER: ').encode()
#     chat_socket.sendall(data + b'\n')
#     print('WAITING FOR CLIENT...')
#     data = b''
#     while b'\n' not in data:
#         data += chat_socket.recv(1024)
#     print('CLIENT WROTE: ' + data.decode())

# modified chat_server
import socket

listen_socket = socket.socket()
listen_socket.bind(('127.0.0.1', 29126))
listen_socket.listen()

chat_socket, addr = listen_socket.accept()
while True:
    data = input('INPUT SERVER: ').encode()
    chat_socket.sendall(data + b'\n')
    if b'quit' in data:
        chat_socket.close()
        listen_socket.close()
        break
    print('WAITING FOR CLIENT...')
    data = b''
    while b'\n' not in data:
        data += chat_socket.recv(1024)
    if b'quit' in data:
        print('CLIENT DISCONNECTED...')
        chat_socket.close()
        listen_socket.close()
        break
    print('CLIENT WROTE: ' + data.decode())
