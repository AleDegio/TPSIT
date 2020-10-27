/*
Alessia De Giovannini 
Esercizio 5
Creare un programma che simuli l'acquisto dei biglietti di un cinema avente due casse
I biglietti disponibili sono prefissati (risorsa condivisa)
All'avvio vengono generati n clienti/threads "per la cassa1 e per la cassa2" per procedere all'acquisto.
    - Gestire la situazione in cui vengono generati x clienti per cassa1 e y clienti per cassa2
Ogni cliente:
    - accede alla risorsa "biglietti disponibili" in modalit� ESCLUSIVA
    - random, acquista un numero di biglietti compreso tra 1 e 5
    - infine, stampa un messaggio a video indicando
        1. Quanti biglietti ha tentato di acquistare
        2. Quanti biglietti ha di fatto acquistato
        3. Quanti biglietti sono ancora disponibili
    - prevedere la possibilit� in cui:
        1. non tutti i clienti riescano ad acquistare x biglietti (in questo caso acquistare i biglietti residui)
        2. i biglietti siano completamente esauriti
La rispettiva cassa, al termine di ogni acquisto (o tentativo di acquisto), valuta, con probabilit� 1/2 (50% o random val 0-1),
se far 'passare' il cliente subito successivo alla medesima fila oppure dare la precedenza al cliente in fila sull'altra cassa
Esempio esecuzione:
> Sono il cliente 489737546 in fila alla cassa1 e voglio acquistare 4 biglietti:
> biglietti acquistati: 4
> biglietti disponibili: 96
> Sono il cliente 794632639 in fila alla cassa2 e voglio acquistare 3 biglietti:
> biglietti acquistati: 3
> biglietti disponibili: 93
> Sono il cliente 876432834 in fila alla cassa2 e voglio acquistare 10 biglietti:
> biglietti acquistati: 10
> biglietti disponibili: 83
....
> Sono il cliente 982374984 in fila alla cassa1 e voglio acquistare 8 biglietti:
> biglietti acquistati: 2
> biglietti disponibili: 0
> Sono il cliente 876865756 in fila alla cassa2 e voglio acquistare 10 biglietti:
> biglietti acquistati: 0
> biglietti disponibili: 0
*/
#include <stdio.h>
#include <pthread.h>
#include <unistd.h>
#include <stdlib.h>


int n_biglietti = 100;
pthread_mutex_t m = PTHREAD_MUTEX_INITIALIZER;
int precedenza1 = 0;
int precedenza2 = 0;

void* cassa(void* args){
	int nCassa = *((int*)args);
	int prova = 0;

	pthread_mutex_lock(&m);

	int daComprare = 1 + rand()%5;
	printf("Sono il cliente %u in fila alla cassa%d e voglio acquistare %d biglietti\n", pthread_self(), nCassa, daComprare);
	if(n_biglietti == 0){
		printf("Biglietti acquistati 0\n");
	}else if(n_biglietti>0 && daComprare<=n_biglietti){
		printf("Biglietti acquistati %d\n", daComprare);
		n_biglietti = n_biglietti - daComprare;
	}

	printf("Biglietti disponibili %d\n\n", n_biglietti);
	cont ++;
	if(nCassa == 1){
		precedenza1 = rand() % 2;
	}else{
		precedenza2 = rand() % 2;
	}

	pthread_mutex_unlock(&m);
	pthread_exit(NULL);
}

int main(int argc, char **argv){
	pthread_t tCassa1[10];
	pthread_t tCassa2[10];
	int cassa1 = 1;
	int cassa2 = 2;
	int i;

	srand(time(NULL));

	for(i = 0; i<10; i++){

		if(precedenza1 == 1 && precedenza2 == 1){
			printf("\nil cliente della fila 2 sta andando alla cassa1 e viceversa\n");
			pthread_create(&tCassa2[i], NULL, (void*)cassa, (void *) &cassa1);
			pthread_create(&tCassa1[i], NULL, (void*)cassa, (void *) &cassa2);
		}else if(precedenza1 == 1 && precedenza2 == 0){
			printf("\nil cliente della fila 2 sta andando alla cassa1\n");
			pthread_create(&tCassa2[i], NULL, (void*)cassa, (void *) &cassa1);
			//continua con quello della propria fila
			pthread_create(&tCassa1[i], NULL, (void*)cassa, (void *) &cassa1);
		}else if(precedenza1 == 0 && precedenza2 == 1){
			printf("\nil cliente della fila 1 sta andando alla cassa2\n");
			pthread_create(&tCassa1[i], NULL, (void*)cassa, (void *) &cassa2);
			//continua con quello della propria fila
			pthread_create(&tCassa2[i], NULL, (void*)cassa, (void *) &cassa2);
		}else{
			printf("\nognuno dei clienti sta andando nella propria cassa\n");
			pthread_create(&tCassa1[i], NULL, (void*)cassa, (void *) &cassa1);
			pthread_create(&tCassa2[i], NULL, (void*)cassa, (void *) &cassa2);
		}

	}

	for(i=0; i<10; i++){
        	pthread_join(tCassa1[i], NULL);
		pthread_join(tCassa2[i], NULL);
	}
	printf("Acquisto terminato\n");
	return 0;
}
