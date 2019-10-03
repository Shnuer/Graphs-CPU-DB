import socket



def writer(sock):
    file=open("log.txt","w")      #you can specify a path for the file here, or a different file name
    while(1):
        try:
            output=sock.recv(500)
            file.write(output)
        except:
            file.close()

try:
    x=socket.socket()
    x.bind(("127.0.0.1",1339))    # Enter IP address and port according to your needs ( replace 127.0.0.1 and 1339 )
    x.listen(2)                   # This will accept upto two connections, change the number if you like
    sock,b=x.accept()
    writer(sock)
except:
    print("bye")
    exit()