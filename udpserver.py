from socket import *

serverPort = 10000

serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind((gethostbyname(gethostname()), serverPort))
print(f'Server is ready')
while True:
    msg, addr = serverSocket.recvfrom(1024)
    msgModified = msg.decode().lower()
    serverSocket.sendto(msgModified.encode(), addr)