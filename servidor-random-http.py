"""
Script que devuelve direcciones aleatorias
"""
#!/usr/bin/python

import socket
import random


mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
print socket.gethostname()
mySocket.bind((socket.gethostname(), 1234))

# 5 respuestas maximo
mySocket.listen(5)

try:
    while True:
        print 'Waiting for connectios'
        (recvSocket, address) = mySocket.accept()
        print 'Request received: '
        print recvSocket.recv(2048)
        link = str(random.randrange(1000000000))
        print 'Answering back...'
        recvSocket.send("HTTP/1.1 200 OK\r\n\r\n" + "<html><body><h1>Hola </h1>" +
                        "<a href='" + link + "'>dame otra</a>" + "</body></html>" + "\r\n")
        recvSocket.close()
except KeyboardInterrupt:
    print "Closing binded socket"
    mySocket.close()
