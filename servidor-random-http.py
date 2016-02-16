"""
Script que devuelve direcciones aleatorias
"""
#!/usr/bin/python

import socket
import random


mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
print socket.gethostname()
mySocket.bind(('localhost', 1234))
# mySocket.bind((socket.gethostname(), 1234))

# 5 respuestas maximo
mySocket.listen(5)

try:
    while True:
        print 'Waiting for connections'
        (recvSocket, address) = mySocket.accept()
        print 'Request received: '
        print recvSocket.recv(2048)
        link = str(random.randint(1, 1000000000))
        print 'Answering back...'
        recvSocket.send("HTTP/1.1 200 OK\r\n\r\n" +
                        "<html><body><h1>Hola </h1>" +
                        "<a href='http://localhost:1234/" 
                        + link + "'>dame otra</a>" +
                        "</body></html>" + "\r\n")
        recvSocket.close()
except KeyboardInterrupt:
    print "Closing binded socket"
    mySocket.close()
