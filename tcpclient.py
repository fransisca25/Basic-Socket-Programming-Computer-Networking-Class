from socket import *

serverIP = input('Input the IP Address of the server: ')
serverPort = int (input('Input the port number to connect: '))

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverIP, serverPort))
msg = input('Type your message all in uppercase: ')
clientSocket.send(msg.encode())
msgModified = clientSocket.recv(1024)
print('Here is the modified message: ', msgModified.decode())
clientSocket.close()