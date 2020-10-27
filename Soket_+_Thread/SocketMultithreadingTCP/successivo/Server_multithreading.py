"""
Alessia De Giovannini
Server Multithreading TCP 2
"""
import socket               
import threading 

#classe utilizzata dalla classe server che starta un thread che gestisca ogni iterazione con un ipotetico client
class ClientThread(threading.Thread):
    
    def __init__(self, address, conn):
        threading.Thread.__init__(self)
        self.clientConn = conn
        self.address = address
        print ("NUOVA CONNESSIONE DA ", address)

    def run(self):
        print("CONNESSO A: ", self.address)
        msg = ''
        while True:
            data = self.clientConn.recv(2048)
            msg = data.decode()
            if msg == "close":
                break
            else:
                print("DAL CLIENT", self.address, "", msg)
                self.clientConn.send(bytes(msg,'UTF-8'))

        print("IL CLIENT", self.address, ": si e' disconnesso")
        self.clientConn.close()
        

class Server():
    def __init__(self, host, port):
        self.host = host
        self.port = port

        self.serverSocket = socket.socket()
        self.serverSocket.bind((host, port))
       
        
    def inizia(self,):
        print("Server partito")
        print("In attesa di client")
        while True:
            self.serverSocket.listen(5)
            conn, addr = self.serverSocket.accept()
            clientThread = ClientThread(addr, conn) #creo il thread delle classe sopra definita
            clientThread.start() #richiama il metodo run della classe ClientThread


def main():
    server = Server("127.0.0.1", 50007)
    server.inzia()

if __name__ == "__main__":
    main()