import socket

s = socket.socket()
s.connect(('127.0.0.1',1234))
while True:
    str = input("S: ")
    s.send(str.encode());
    if(str == "Bye" or str == "bye"):
        break
    print ("N:",s.recv(1024).decode())
s.close()