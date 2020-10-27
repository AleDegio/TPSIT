"""
Alessia De Giovannini
Telefono senza fili UDP
Server 
"""
import socket

def server():
    ip = "127.0.0.1" 
    porta = 7000
    bufferSize = 1024

    #Creazione del Socket Server  
    socketServer = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    socketServer.bind((ip, porta))
    print("il signor Server è in attesa")

    #Fase di Ascolto 
    datiSocket = socketServer.recvfrom(bufferSize)
    #recvfrom => istruzione bloccante 
    #ovvero il programma si ferma qui 
    #perchè il Server rimane in ascolto 
    msgC = datiSocket[0]
    address = datiSocket[1] #ip + porta 
    msgClient = "{}".format(str(msgC,'utf-8'))
    ipClient = "Client: {}".format(address)

    return msgClient

def main(): 
    msgClient = server()
    print(msgClient)

if __name__ == "__main__":
    main()