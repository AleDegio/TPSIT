"""
Alessia De Giovannini
Gestione thread  
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

    logging.info("PADRE: creazione del thread") #unico paramentro del metodo info 

    #Creazione di un thread 

    #Inizializzazione del thread
    #target = nome fnzione che deve eseguire il thread
    #args contiene valori da trasmettere al thread 
    x = threading.Thread(target=fn_thread, args=(1, )) 
    #Avviamento del thread
    x.start() 

    logging.info("PADRE: aspetto la terminazione del thread creato")
    x.join()

    logging.info("PADRE: fine")
