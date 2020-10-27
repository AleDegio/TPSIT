"""
Alessia De Giovannini
Client ECHO
"""
import socket

msgPerClient = "ECHO"
bytesSend = str.encode(msgPerClient)
porta = ("127.0.0.1", 6000) #dati del signor Server
bufferSize = 1024

#Creazione del Socket Client 
socketClient = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #AF_INET = IPV4

#Mandare un msg al signor Server 
socketClient.sendto(bytesSend, porta)
msgPerServer = socketClient.recvfrom(bufferSize)
msg = "Messaggio per il signor Server {}".format(msgPerServer[0])

print(msg)

#Chiusura del Socket Client
socketClient.close()