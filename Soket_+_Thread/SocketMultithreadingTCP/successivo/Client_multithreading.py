"""
Alessia De Giovannini
Client Multithreading TCP 2
"""
import socket

def clientECHO():
    host = "127.0.0.1"
    port = 50007
    bufferSize = 1024 

    #Creazione del Socket Client 
    sc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #Connessione 
    sc.connect((host, port))

    while True:
        msg = input("Messagio: ")
        #Mandare msg al signor Server 
        sc.sendall(msg.encode())
        if msg == "close":
            break
        data = sc.recv(bufferSize)
        print("Ricevuto: ", data.decode("utf-8"))
        

    #Chiusura Socket Client 
    sc.close()

def main(): 
    clientECHO()

if __name__ == "__main__":
    main()



