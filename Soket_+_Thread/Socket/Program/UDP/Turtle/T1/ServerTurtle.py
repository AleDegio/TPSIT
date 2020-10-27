"""
Alessia De Giovannini
Server Turtle
"""
import socket
import random
import turtle
import time

def eseguiComandi(msg, tartaruga):
    vet = msg.split("_")
    comando = vet[0]
    val = int(vet[1])
    """Comandi: forward_x backward_y left_z right_k"""
    if comando == "forward":
        tartaruga.forward(val)
    elif comando == "backward":
        tartaruga.backward(val)
    elif comando == "left":
        tartaruga.left(val)
    elif comando == "right":
        tartaruga.right(val)

def creaTartaruga(address, diz):
    color = ["blue", "red", "yellow"]
    if (address not in diz):
        tartaruga = turtle.Turtle()
        tartaruga.penup()
        tartaruga.setx(random.randint(0, 20))
        tartaruga.color(color[random.randint(0,2)])
        tartaruga.sety(random.randint(0, 20))
        tartaruga.pendown()
        diz[address] = tartaruga

def server():
    ip = "127.0.0.1"
    porta = 20001
    bufferSize = 1024
    msgClientServer = "Salve signor Client"
    bytesSend = str.encode(msgClientServer)
    
    #Creazione del Socket Server  
    socketServer = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    socketServer.bind((ip, porta))
    print("il signor Server la puo' ricevere")

    diz = {}
    ex = False
    #Fase di Ascolto 
    while(True):
        datiSocket = socketServer.recvfrom(bufferSize)
        msgC = datiSocket[0]
        address = datiSocket[1] #ip + porta 

        creaTartaruga(address[1], diz)
        
        msgClient = "Messaggio dal signor Client:{}".format(msgC)
        ipClient = "IP del signor Client:{}".format(address)

        eseguiComandi(str(msgC, "utf-8"), diz[address[1]])
    socketServer.close()

def main(): 
    server()

if __name__ == "__main__":
    main()