"""
Alessia De Giovannini
Client ECHO TCP 
"""
import socket

def clientECHO():
    host = "127.0.0.1"
    port = 50007
    bufferSize = 1024 
    msg = "ECHO"    #Messaggio di ECHO

    #Creazione del Socket Client 
    sc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #Connessione 
    sc.connect((host, port))

    #Mandare msg ECHO al signor Server 
    sc.sendall(msg.encode())
    data = sc.recv(bufferSize)

    #Chiusura Socket Client 
    sc.close()

    print ("Ricevuto: ", data)

def main(): 
    clientECHO()

if __name__ == "__main__":
    main()