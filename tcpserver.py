from socket import *

print (gethostbyname(gethostname()))
serverPort = 10000

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind((gethostname(), serverPort))
serverSocket.listen(1)
print(f'Server is ready')

while True:
    connectionSocket, addr = serverSocket.accept()
    print(f'Connection has been established!')
    msg = connectionSocket.recv(1024).decode()
    msgCaps = msg.lower()
    connectionSocket.send(msgCaps.encode())
    if not msg: 
        break

    connectionSocket.close()