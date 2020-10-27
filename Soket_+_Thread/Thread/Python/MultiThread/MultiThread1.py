"""
Alessia De Giovannini
Gestione thread multipli 1
"""
import threading
import logging      #come Print 
import time

def fn_thread(val):
    logging.info("Thread %s: inizio", val)
    time.sleep(2) #attende 2 secondi 
    logging.info("Thread %s: fine", val)

if __name__ == "__main__":
    #Visualizzazione stringa msg 
    format = "%(asctime)s: %(message)s:" #visibile nella consolle 
    logging.basicConfig(format = format, level=logging.INFO, datefmt="%H:%M:%S")

    logging.info("PADRE: creazione dei threads") #unico paramentro del metodo info 

    #Creazione dei threads 
    threads = list()
    for i in range(5):
        logging. info("PADRE: creazione ed avvio thread %d", i)
        #Inizializzazione del thread
        #target = nome fnzione che deve eseguire il thread
        #args contiene valori
        x = threading.Thread(target=fn_thread, args=(i, ))
        threads.append(x)
        #Avviamento del thread
        x.start()

    for i, t in enumerate(threading):  
        logging.info("PADRE: prima dell'attesa del thread %d", i)
        t.join() 
        logging.info("PADRE: thread %d terminato", i)

    logging.info("PADRE: fine")
