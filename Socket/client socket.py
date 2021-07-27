import socket as s

def create_client():
    client_socket = s.socket()

    addr = input('ipv4:')
    port = int(input('port:'))

    return addr, port

#client_socket.connect((addr, port))
# data = b''
# while b'\n' not in data:
#     data += client_socket.recv(1024)
# print(data)
# client_socket.sendall(b'Hello Mr Ng!'+ data)]

connect = False
while True:
    if not connect:
        client_socket = s.socket()
        addr, port = create_client()
        client_socket.connect((addr, port))
        connect = True
    # send message to server (client to server)
    toServer = input('Enter message: ').encode()
    client_socket.sendall(toServer + b'\n')

    print('Waiting for server...')
    fromServer = b''
    while b'\n' not in fromServer:
        fromServer += client_socket.recv(1024)
    message = fromServer.decode()
    if message == 'Shutting down\n':
        connect = False
        client_socket.close()
        print('Disconnected')
        while True:
            cont = input('Connect to a new server? (Y/N): ').title()
            if cont == 'Y' or cont == 'N':
                break
            print('Error, answer must be Y or N')

        if cont == 'Y':
            continue
        else:
            break
    else:
        print('Server wrote: ' + fromServer.decode())