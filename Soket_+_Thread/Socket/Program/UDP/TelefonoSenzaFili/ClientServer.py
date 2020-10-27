"""
Alessia De Giovannini
Telefono senza fili UDP
Cilent Server
"""
import socket

def client(msgClient):
    #msgPerClient = str(input("Scrivi la parola: "))
    bytesSend = str.encode(msgClient)
    porta = ("127.0.0.1", 7000)
    bufferSize = 1024

    #Creazione del Socket Client 
    socketClient = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    #Mandare un msg al signor Server 
    socketClient.sendto(bytesSend, porta)

def server():
    ip = "127.0.0.1" #my
    porta = 7000
    bufferSize = 1024

    #Creazione del Socket Server  
    socketServer = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    socketServer.bind((ip, porta))
    print("il signor Server la puo' ricevere")

    #Fase di Ascolto 
    datiSocket = socketServer.recvfrom(bufferSize)
    #recvfrom => istruzione bloccante 
    #ovvero il programma si ferma qui 
    #perchè il Server rimane in ascolto 
    msgC = datiSocket[0]
    address = datiSocket[1] #ip + porta 
    msgClient = "Parola: {}".format(str(msgC,'utf-8'))
    ipClient = "Client: {}".format(address)
    
    print("[" + ipClient + "]" + " " + msgClient)
    return msgClient

def main(): 
    msgClient = server()
    client(msgClient)

if __name__ == "__main__":
    main()