import socket
s = socket.socket()
print('Scoket succesfully created')
port = 56789
s.bind(('', port))
print(f'socket binded to port{port}')
s.listen(5)
print('socket is listing')
while True:
    C, addr = s.accept()
    print('Got connection from', addr)
    message = ('Thank you for connecting')
    C.send(message.encode())
    C.close()