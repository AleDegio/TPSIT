"""
Alessia De Giovannini
Client Turtle 
"""
import socket

def comandi():
    x = input("Comandi: forward_x backward_y left_z right_k \n")
    return x

def client():
    ex = False
    porta = ("127.0.0.1", 20001)
    bufferSize = 1024

    #Creazione del Socket Client 
    socketClient = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while ex==False:
        msgPerClient = comandi()
        if msgPerClient=="Exit":
            ex = True
        else:
            bytesSend = str.encode(msgPerClient)

            #Mandare un msg al signor Server 
            socketClient.sendto(bytesSend, porta)
    socketClient.close()

def main(): 
    client()

if __name__ == "__main__":
    main()