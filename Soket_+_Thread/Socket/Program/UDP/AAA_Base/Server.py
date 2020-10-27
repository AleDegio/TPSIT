"""
Alessia De Giovannini
Server
"""
import socket

def server():
    ip = "192.168.1.58"
    porta = 20001
    bufferSize = 1024

    msgClientServer = "Salve signor Client"
    bytesSend = str.encode(msgClientServer)

    #Creazione del Socket Server  
    socketServer = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

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
        socketServer.sendto(bytesSend, address)

def main(): 
    server()

if __name__ == "__main__":
    main()