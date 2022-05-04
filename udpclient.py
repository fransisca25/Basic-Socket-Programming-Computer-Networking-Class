from socket import *

serverIP = gethostbyname(gethostname())
serverPort = int (input('Input the port number to connect: '))

clientSocket = socket(AF_INET, SOCK_DGRAM)
msg = input('Input your message all in uppercase: ')
clientSocket.sendto(msg.encode(), (serverIP, serverPort))
msgModified, addr = clientSocket.recvfrom(1024)
print(msgModified.decode())
clientSocket.close()