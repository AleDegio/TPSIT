"""
Alessia De Giovannini
Client Multithreading TCP Turtle
"""
import socket
import turtle
import random
import time

def clientTurtle():
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

        comandi, valori = convertString(data)
        tartaruga = creaTartaruga()
        
        for i in range(0, len(comandi)):
        #se il numero e' di 3 cifre lo divido per 3 
        #altrimenti uscirebbe fuori dallo schermo
            if len(valori[i]) == 3:
                val = int(valori[i]) / 3
            else:
                val = int(valori[i])
            eseguiComandi(comandi[i], val, tartaruga)

        turtle.done()
    else:
        print(data)
    #Chiusura Socket Client 
    sc.close()
    
#converte la stringa ricevuta dal server in comandi per la turtle
#esempio: "F100R20" -> forward 100 right 20
def convertString(data):
    numeri = "012456789"
    valori = []
    comandi = []
    i = 0
    while i < len(data):
        valore = ""
        if data[i] not in numeri:
            if data[i] == "F":
                comandi.append("forward")
            elif data[i] == "B":
                comandi.append("backward")
            elif data[i] == "R":
                comandi.append("right")
            elif data[i] == "L":
                comandi.append("left")
        else: 
            while i<len(data) and data[i] in numeri:
                valore+= data[i]
                i = i + 1 
            i = i - 1
        if valore is not "":
            valori.append(valore)
        i = i + 1; 
    return comandi, valori

def eseguiComandi(comando, valore, tartaruga):
    #Dizionario di comandi 
    """Comandi: forward_x backward_y left_z right_k"""
    comandi = {"forward": "tartaruga.forward(valore)", "backward": "tartaruga.backward(valore)",
     "left": "tartaruga.left(valore)", "right": "tartaruga.right(valore)"}
    eval(comandi[comando])

    """
    if comando == "forward":
        tartaruga.forward(val)
    elif comando == "backward":
        tartaruga.backward(val)
    elif comando == "left":
        tartaruga.left(val)
    elif comando == "right":
        tartaruga.right(val)
    """

def creaTartaruga():
    color = ["blue", "red"]
    tartaruga = turtle.Turtle()
    tartaruga.penup()
    tartaruga.color(color[random.randint(0,1)])
    tartaruga.setx(0)
    tartaruga.sety(0)
    tartaruga.pendown()
    return tartaruga
   
def main(): 
    clientTurtle()

if __name__ == "__main__":
    main()
