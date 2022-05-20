import socket

s = socket.socket()
port = 1234
s.bind(('127.0.0.1', port))
s.listen(5)
c, addr = s.accept()
print ("Socket Up and running with a connection from",addr)
while True:
    rcvdData = c.recv(1024).decode()
    print ("S:",rcvdData)
    sendData = input("N: ")
    c.send(sendData.encode())
    if(sendData == "Bye" or sendData == "bye"):
        break
c.close()