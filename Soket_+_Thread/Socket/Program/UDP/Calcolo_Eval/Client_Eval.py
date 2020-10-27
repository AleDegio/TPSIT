"""
Alessia De Giovannini
Client Calcolo (Eval)
"""
import socket

msgPerClient = str(input("Inserisci un'operazione: "))
bytesSend = str.encode(msgPerClient)
porta = ("79.31.222.112", 6000)
bufferSize = 1024

#Creazione del Socket Client 
socketClient = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#Mandare un msg al signor Server 
socketClient.sendto(bytesSend, porta)
msgPerServer = socketClient.recvfrom(bufferSize)
msg = "Risultato: " + str(msgPerServer[0],'utf-8')

print(msg)