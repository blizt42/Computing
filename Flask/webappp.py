import random as ran
import socket as s

EOL = b'\r\n'

colours = [
    'red', 'orange', 'blue', 'purple', '#C0C000', #dark yellow
    '#00C000' #dark green
]

Messages = ['Hellow', 'hi']

listen_socket = s.socket()
listen_socket.bind(('127.0.0.1', 8000))
listen_socket.listen()

def handle_request(new_socket):
    request = b''
    
    while EOL not in request:
        
        received = new_socket.recv(1024)
        if received == b'':
            new_socket.close()
            return
        request += received
    
    index = request.index(EOL)
    first_line = request[:index].decode()
    path = first_line.split()
    
    response = b'HTTP/1.1 200 OK' + EOL
    
    if path =='/css':
        border_colour = ran.choice(Colours)
        text_colour = ran.choice(Colours)
        body = 'p {{ border: 5 px solid {0}; color: {1};'
        body += 'font-size : 72px; padding: 20px; }}'
        body = body.format(border_colour, text_colour)
        body = body.encode()
        
        resp += b'Content-Type: text/css' + EOL
        resp += b'Content-Length: '
        resp += str(len(body)).encode() + EOL
        
    else:
        msg = ran.choice(Messages)
        body = '<!DOCTYPE html>\n<html>'
        body += '<head><title>{0}</title>'
        body += '<link rel="stylesheet" href="/css"></head>'
        body += '<body><p>{0}</p></body></html>'
        body = body.format(msg).encode()

while True:
    new_socket, addr = listen_socket.accept()
    
    handle_request(new_socket)
