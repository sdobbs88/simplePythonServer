# using the following URL: http://localhost:1853/index.html
from socket import *


def main():
    serverPort=1853
    serverSocket = socket(AF_INET, SOCK_STREAM)
    
    #Prepare a server socket
    serverSocket.bind(('',serverPort))
    serverSocket.listen(1)
    print ('The web server is up on port:',serverPort)
    while True:
        
        #Establish the connection
        print ('Ready to serve...')
        connectionSocket, addr = serverSocket.accept()
        try:
            message = connectionSocket.recv(1024)
            print (message,'::', message.split()[0],':',message.split()[1])
            filename = message.split()[1]
            print (filename,'||',filename[1:])
            f = open(filename[1:])
            outputdata = f.read()
            print (outputdata)
            
            #Send one HTTP header line into socket
            connectionSocket.send(bytes("HTTP/1.1 200 OK\r\n\r\n","UTF-8"))
            connectionSocket.send(bytes(outputdata, "UTF-8"))
            connectionSocket.close()
            
        except IOError:
            pass
        
            print ('404 Not Found')
            connectionSocket.send(bytes("HTTP/1.1 404 Not Found\r\n\r\n","UTF-8"))
            
        #TEMP BREAK
        break
    pass
if __name__ == '__main__':
    main()