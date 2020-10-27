/*
Alessia De Giovannini
Esercizio CSV
Creare un programma in linguaggio C che legga il file vgsales.csv
e lo importi in un array di strutture.
Ogni riga contiene i campi separati da virgole,
per cui puo' essere comodo creare una funzione split
che dalla riga letta ritorni la struttura valorizzata.
Creare la funzione split (restituisce la struttura della riga)
*/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define DIM 1024
#define MIL 1000
#define  VIRG ","

typedef struct tabella{
    int Rank;
    char *Name;
    char *Platform;
    int Year;
    char *Genre;
    char *Publisher;
    float NA_Sales;
    float EU_Sales;
    float JP_Sales;
    float Other_Sales;
    float Global_Sales;
}Struttura;

int leggiTabella(Struttura tabella[DIM], FILE *fp){
    int i=0;
    char *dup;  //variabile per la duplicazione delle stringhe
    char space[10];
    char *field;  //puntatore al primo char trovato

    /*
    strtok();
    Rompe la stringa in una serie di char utilizzando un separatore.
    Restituisce un puntatore al primo char trovato.
    Viene restituito un puntatore NULL se non sono presenti char.
    *//*
    atoi();
    Converte la stringa in un int.
    Restituisce il numero convertito come int.
    Se non è possibile eseguire alcuna conversione, restituisce zero.
    *//*
    strdup();
    Duplica la stringa e restituisce un puntatore
    ad una stringa di byte con terminazione NULL.
    */
    //legge fino a quando ci sono rige nel file
    while (fgets(space, DIM, fp)) {   //fgets prende anche gli spazzi
      field=strtok(space, VIRG);
      tabella[i].Rank=atoi(field);
      field=strtok(NULL, VIRG);
      dup=strdup(field/*tabella[i].Name*/);
      field=strtok(NULL, VIRG);
      dup=strdup(field/*tabella[i].Platform*/);
      field=strtok(NULL, VIRG);
      tabella[i].Year=atoi(field);
      field=strtok(NULL, VIRG);
      dup=strdup(field/*tabella[i].Genre*/);
      field=strtok(NULL, VIRG);
      dup=strdup(field/*tabella[i].Publisher*/);
      field=strtok(NULL, VIRG);
      tabella[i].NA_Sales=atoi(field);
      field=strtok(NULL, VIRG);
      tabella[i].EU_Sales=atoi(field);
      field=strtok(NULL, VIRG);
      tabella[i].JP_Sales=atoi(field);
      field=strtok(NULL, VIRG);
      tabella[i].Other_Sales=atoi(field);
      field=strtok(NULL, VIRG);
      tabella[i].Global_Sales=atoi(field);
      if(i%MIL==0){
        printf("RECORD--->%d, %s, %s, %d, %s, %s, %f, %f, %f, %f, %f\n",
				tabella[i].Rank,tabella[i].Name,
				tabella[i].Platform,tabella[i].Year,tabella[i].Genre,
				tabella[i].Publisher,tabella[i].NA_Sales,tabella[i].EU_Sales,
				tabella[i].JP_Sales,tabella[i].Other_Sales,tabella[i].Global_Sales);
		  }
		i++;
    }
    return i;
}


int main(){
    FILE *fp;
    int i=0;
    Struttura tabella[DIM];
    char riga[20];

    fp=fopen("vgsales-Copia.txt", "r");
    if(fp==NULL){
        printf("il file non esiste\n");
    }else{
        printf("il file e' stato aperto\n");
    }
    i=leggiTabella(tabella, fp);

    printf("Record letti: %d\n", i);
    printf("\nil file e' stato chiuso");
    fclose(fp);
}
