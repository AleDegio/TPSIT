"""
Alessia De Giovannini
Telefono senza fili 
Cilent Server TCP
"""
import socket

def client(data):
    #msgPerClient = str(input("Scrivi la parola: "))
    bytesSend = str.encode(data)
    porta = ("127.0.0.1", 7001)
    bufferSize = 1024

    #Creazione del Socket Client 
    socketClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #Mandare un msg al signor Server 
    socketClient.sendto(bytesSend, porta)

def server():
    host = "127.0.0.1"
    port = 7000
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

    
    print("[" + addr + "]" + " " + data)
    return data

def main(): 
    data = server()
    client(data)

if __name__ == "__main__":
    main()