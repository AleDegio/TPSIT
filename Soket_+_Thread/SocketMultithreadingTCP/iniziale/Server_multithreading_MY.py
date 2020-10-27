"""
Alessia De Giovannini
Server Multithreading TCP 1
"""
import socket               
import _thread

def conn_client(conn,addr):
    while True:
        msg = conn.recv(1024)
        print(addr, ' >> ', msg.decode("utf-8"))
        msg = input('SERVER >> ')
        
        conn.send(str.encode(msg))
    conn.close()

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
        _thread.start_new_thread(conn_client, (conn, addr))
        
    s.close()