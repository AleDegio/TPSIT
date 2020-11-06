"""
Alessia De Giovannini
Server Alphabot 
"""
import socket               
import _thread
import sqlite3


def conn_client(conn):
    msg = conn.recv(1024)
    msg = msg.decode("utf-8")
    end, start = msg.split(",")

    #connessione al db
    print()
    connDB = sqlite3.connect('percorsi.db', check_same_thread=False)
    print("Connessione con DB avvenuta")
    
    #Prima Query
    cursor = connDB.execute("SELECT luoghi.id FROM luoghi WHERE luoghi.nome = ?", (end,))
    idEnd = cursor.fetchone()[0] #prende la prima riga della tabella e con '[0]' prendo solo il primo campo, 
                                 #se eseguo un'altra fetchone() prendo la seconda riga ecc...

    cursor = connDB.execute("SELECT luoghi.id FROM luoghi WHERE luoghi.nome = ?", (start,))
    idStart = cursor.fetchone()[0]
    
    print("End: " + str(idEnd))
    print("Start: " + str(idStart))

    #Seconda Query 
    cursor = connDB.execute("SELECT inizio_fine.id_percorso FROM inizio_fine WHERE id_start = ? AND id_end = ?", (idStart, idEnd)) 
    idpercorso = cursor.fetchone()[0]
    print("ID percorso: " + str(idpercorso))

    #Terza Query
    cursor = connDB.execute("SELECT percorsi.percorso FROM percorsi WHERE percorsi.id = ?", (idpercorso,)) 
    percorso = cursor.fetchone()[0]
    print("Percorso: " + percorso)

    #invio percorso all'ALPHABOT 
    conn.send(bytes(percorso,'UTF-8'))

    conn.close()
    connDB.close()

if __name__ == "__main__":
    s = socket.socket()
    host = "127.0.0.1" 
    port = 50007 

    print("inizializzazione")
    print("in attesa di Client")

    s.bind((host, port))
    s.listen(5)     #Max 5 Client contemporaneamente 

    while True:
        conn, addr = s.accept() 
        _thread.start_new_thread(conn_client, (conn,))
        
    s.close()

    