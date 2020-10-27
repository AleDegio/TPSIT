"""
Alessia De Giovannini
Server ECHO
"""
import socket

ip = "127.0.0.1"  #127.0.0.1
porta = 6000
bufferSize = 1024

#Creazione del Socket Server 
socketServer = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #AF_INET = IPV4
socketServer.bind((ip, porta))
print("il signor Server la puo' ricevere")

#Fase di Ascolto 
while(True):
    datiSocket = socketServer.recvfrom(bufferSize) 
    #recvfrom => istruzione bloccante 
    #ovvero il programma si ferma qui 
    #perchè il Server rimane in ascolto 
    msgC = datiSocket[0]
    address = datiSocket[1] #ip + porta 
    msgClient = "Messaggio dal signor Client:{}".format(msgC)
    ipClient = "IP del signor Client:{}".format(address)
    
    print(msgClient)
    print(ipClient)

    #Messaggio ECHO al signor Client 
    socketServer.sendto(msgC, address)

#Chiusura del Socket Server
socketServer.close()