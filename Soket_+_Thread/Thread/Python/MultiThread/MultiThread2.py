"""
Alessia De Giovannini
Gestione thread multipli 2
"""
import threading
import logging      #come Print 
import time

def fn_thread(val):
    #una volta che è stata eseguita dal primo thred, questa funz blocca tutti gli altri thread 
    l.acquire()
    logging.info("Thread %s: inizio", val)
    time.sleep(2) #attende 2 secondi 
    logging.info("Thread %s: fine", val)
    #rilascia i thread 
    l.release()
    """l.acquire() e l.release() fanno eseguire un thread alla volta"""

    
if __name__ == "__main__":
    #Visualizzazione stringa msg 
    format = "%(asctime)s: %(message)s:" #visibile nella consolle 
    logging.basicConfig(format = format, level=logging.INFO, datefmt="%H:%M:%S")

    l = threading.Lock() #carica l'ogg lock in modo da poter agire su l

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
