import socket
s = socket.socket()
print("socket created")
s.bind(('Localhost', 9999))
s.listen (3)
print( "waiting for the connection" )
while True:
    c, addr = s.accept()
    name = c.recv(1824).decode()
    print('connected with ', addr, name)
    c.send(bytes('Welcome', 'utf-8'))
    c.close()