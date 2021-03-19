"""
Alessia De Giovannini
Web Server
"""
from flask import Flask, render_template, redirect, url_for, request
import socket
from AlphaBot import *

app = Flask(__name__)
alphaBot = AlphaBot() 

def server():
    body = "name=sinistra"
    content_type="application/x-www-form-urlencoded"
    content_length=len(body)   
    
#decoratote 
@app.route('/', methods=['GET', 'POST'])
def index():
    msg = ""
   
    if request.method == 'POST':
        res = list(request.form)[0] #trasformo il dizionario in un array e prendo il primo elemento
        
        if  res == "su":
            alphaBot.forward() #vado avanti
        elif  res == "giu":
            alphaBot.backward() #vado indietro
        elif res == "sinistra":
            alphaBot.setMotor(50, 0) #ruoto a sinitra
            alphaBot.forward() #vado avanti
        elif res == "destra":
            alphaBot.setMotor(0, 50) #ruoto a destra 
            alphaBot.forward() #vado avanti
            
        #attendo lo spostamento
        print("attendo 2 secondi per lo spostamento")
        time.sleep(2)
        #interrompo lo spostamento
        alphaBot.stop()
        msg = "l'alphabot si e' spostato verso " + res + " ora è pronto ad eseguire un altro comando"
        
    return render_template('index.html', msg=msg)


if __name__ == "__main__":
    app.run(host="127.0.0.1")