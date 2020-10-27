"""
Alessia De Giovannini
Telefono senza fili UDP
Client 
"""
import socket

def client():
    msgPerClient = str(input("Scrivi la parola: "))
    bytesSend = str.encode(msgPerClient)
    porta = ("127.0.0.1", 7000)
    bufferSize = 1024

    #Creazione del Socket Client 
    socketClient = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    #Mandare un msg al signor Server 
    socketClient.sendto(bytesSend, porta)

def main(): 
    client()

if __name__ == "__main__":
    main()