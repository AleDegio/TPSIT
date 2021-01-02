"""
Alessia De Giovannini
Client Multithreading TCP 
"""
import socket
import random
import time

def client1():
    host = "127.0.0.1"
    port = 50007
    bufferSize = 1024 

    #Creazione del Socket Client 
    sc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #Connessione 
    sc.connect((host, port))

    msg = input("inserisci il percorso (es. info2,info1): ")
    #Mandare msg al signor Server 
    sc.sendall(msg.encode())
    data = sc.recv(bufferSize)
    data = data.decode("utf-8")
    cod = data.split(',')[0]
    if cod == "0.0" :
        data = data.split(',')[1].replace(" ", "")
        print(data)
    #Chiusura Socket Client 
    sc.close()
   
def main(): 
    client1()

if __name__ == "__main__":
    main()
