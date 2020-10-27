"""
Alessia De Giovannini
Creare un programma che simuli l'acquisto dei biglietti di un concerto
I biglietti disponibili sono prefissati (risorsa condivisa)
All'avvio vengono generati n clienti/threads che "vanno alla cassa" per procedere all'acquisto.
Ogni cliente:
    - accede alla risorsa "biglietti disponibili" in modalita' ESCLUSIVA
    - random, acquista un numero di biglietti compreso tra 1 e 10 
    - infine, stampa un messaggio a video indicando 
        1. Quanti biglietti ha tentato di acquistare
        2. Quanti biglietti ha di fatto acquistato
        3. Quanti biglietti sono ancora disponibili
    - prevedere la possibilita' in cui:
        1. non tutti i clienti riescano ad acquistare x biglietti (in questo caso acquistare i biglietti residui)
        2. i biglietti siano completamente esauriti
Esempio esecuzione:
> Sono il cliente 489737546 e voglio acquistare 4 biglietti:
> biglietti acquistati: 4
> biglietti disponibili: 96
....
> Sono il cliente 792837528 e voglio acquistare 8 biglietti:
> biglietti acquistati: 2
> biglietti disponibili: 0
> Sono il cliente 876865756 e voglio acquistare 10 biglietti:
> biglietti acquistati: 0
> biglietti disponibili: 0
"""
import threading    #creazione e avvio dei Thread 
import logging      #come Print 
import time
import random

n_biglietti = 100  #Risorsa condivisa: biglietti decrementati ogni volta che vengono acquistati con successo 

def cassa(tD):
    global n_biglietti
    mutex.acquire()
    rnd = random.randint(1,10)
    logging.info("Sono il clienta %d e voglio acquistare %d biglietti",tD ,rnd)
    if n_biglietti==0:
        logging.info("Biglietti acquistati: 0")
    elif rnd<=n_biglietti:
        logging.info("Biglietti acquistati: %d", rnd)
        n_biglietti=n_biglietti-rnd
    elif rnd>n_biglietti:
        logging.info("Biglietti acquistati: %d", n_biglietti)
        n_biglietti=0
    logging.info("Biglietti disponibili: %d", n_biglietti)
    mutex.release()

if __name__ == "__main__":
    #Visualizzazione stringa msg 
    format = "%(asctime)s: %(message)s:" #visibile nella consolle 
    logging.basicConfig(format = format, level=logging.INFO, datefmt="%H:%M:%S")

    #lista di Thread 
    threads = []
    for i in range(3):
        logging.info("Apertura cassa tra %d..", i)
        time.sleep(1)
    #Inizializzazione della Mutex 
    mutex = threading.Lock()

    for i in range(0,10):
        #Creazione di un thread 
        #Inizializzazione del thread
        #target = nome fnzione che deve eseguire il thread
        #args contiene valori da trasmettere al thread 
        t = threading.Thread(target=cassa, args=((i+1), )) 
        threads.append(t)

        #Avviamento del thread
        t.start() 

        for i, t in enumerate(threads): #enumerate() scorre per quanto e' lunga la lista 
            t.join()

    logging.info("Chiusura cassa")