"""
Alessia De Giovannini
Client Example
"""
import socket

msgFromClient = "Salve signor Server"
bytesToSend = str.encode(msgFromClient)
serverAddressPort = ("192.168.1.58", 20001)
bufferSize = 1024

# Create a UDP socket at client side
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Send to server using created UDP socket
UDPClientSocket.sendto(bytesToSend, serverAddressPort)
msgFromServer = UDPClientSocket.recvfrom(bufferSize)
msg = "Messaggio del Server {}".format(msgFromServer[0])

print(msg)