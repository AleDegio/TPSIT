"""
Alessia De Giovannini
Client Sensori 
"""
import time
from AlphaBot import *

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
  
    tempo_attesa = int(valore) / 100  
    
    comandi = {"forward": "alphaBot.forward()", "backward": "alphaBot.backward()",
     "left": "alphaBot.setMotor(50, 0)", "right": "alphaBot.setMotor(0, 50)"}
     
    if(comando is not "left" and comando is not "right"):
        eval(comandi[comando]) #evita di fare le if annidate 
    else:
        eval(comandi[comando])
        alphaBot.forward()

    print("L'aphabot si sta muovendo per: " + str(tempo_attesa) + " secondi (attendo)")
    #attendo lo spostamento
    time.sleep(tempo_attesa)
    #interrompo lo spostamento
    alphaBot.stop()
