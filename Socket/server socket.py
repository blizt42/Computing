import socket as s

# server is dedicated for connection requests from clients
server = s.socket()
server.bind(('127.0.0.1', 22345))
server.listen() # server will wait if there are no request

client_socket , addr = server.accept()

while True:
    # send message to client (server to client)
    toClient = input('Server message: ').encode()
    client_socket.sendall(toClient + b'\n')

    print(type(toClient), type(b'\n'))

    # Displays message from client
    print('Waiting for client')
    fromClient = b''
    while b'\n' not in fromClient:
        fromClient += client_socket.recv(1024)
    print('Client sent: ' + fromClient.decode())

# while True:
#     client_socket , addr = server.accept()
#     print('connected to :',client_socket,addr)
#     client_socket.sendall(b'Hello!' + b'\n')
#     client_socket.close()