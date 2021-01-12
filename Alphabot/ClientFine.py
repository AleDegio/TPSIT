"""
Alessia De Giovannini
Client Multithreading TCP Fine
"""
import socket
import random
import time
from AlphaBot import *

def client():
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
        alphaBot = AlphaBot() 
        comandi, valori = convertString(data)
        
        for i in range(0, len(comandi)):
            eseguiComandi(comandi[i], valori[i], alphaBot)

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
                valore += data[i]
                i = i + 1 
            i = i - 1
        if valore is not "":
            valori.append(valore)
        i = i + 1; 
    return comandi, valori

def eseguiComandi(comando, valore, alphaBot):
    '''
    Simulo un tempo di attesa per il movimento dell'alphabot in base alla grandezza del valore letto dal db -> es. 800 ---> 8.0 sec 90 ---> 0.9 sec.
    ''' 
    tempo_attesa = int(valore) / 100  
    
    """Comandi: forward backward left right"""
    comandi = {"forward": "alphaBot.forward()", "backward": "alphaBot.backward()",
     "left": "alphaBot.setMotor(50, 0)", "right": "alphaBot.setMotor(0, 50)"}
     
    if(comando is not "left" and comando is not "right"):
        ''' Se il comando è forward o backward eseguo il comando '''
        eval(comandi[comando]) #evita di fare le if annidate 
    else:
        ''' Se il comando è left o right  ruoto e poi faccio andare avanti l'alphabot '''
        eval(comandi[comando])
        alphaBot.forward()

    print("L'aphabot si sta muovendo per: " + str(tempo_attesa) + " secondi (attendo)")
    #attendo lo spostamento
    time.sleep(tempo_attesa)
    #interrompo lo spostamento
    alphaBot.stop()

def main(): 
    client()

if __name__ == "__main__":
    main()
