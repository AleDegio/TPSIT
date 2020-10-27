"""
Alessia De Giovannini
Server ECHO TCP 
"""
import socket

def serverECHO():
    host = "127.0.0.1"
    port = 50007
    bufferSize = 1024

    #Creazione del Socket Server  
    ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    ss.bind((host, port))
    print("il signor Server la puo' ricevere")

    ss.listen()
    conn, addr = ss.accept()
    print ("Connesso a ", addr)

    #Fase di Ascolto 
    while(True):
        data = conn.recv(bufferSize)
        if not data:
            break
        conn.send(data)

    #Chiusura Connessione 
    conn.close()
    #Chiusura Socker Server 
    ss.close()

def main(): 
    serverECHO()

if __name__ == "__main__":
    main()