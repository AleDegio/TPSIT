/*
Alessia De Giovannini
Esercizi 123
*/
#include <stdio.h>
#include <stdlib.h>

typedef struct El{
  int valore;
  struct El* next;  //puntatote referenziato (puntare alla struttura stessa)
};
typedef struct El *El;

//Esercizio 2
void stampaLista(struct El* ListaDiElementi){
    if (ListaDiElementi==NULL){
      printf ("//\n");
    }else{
        printf("%d->", ListaDiElementi->valore);
        stampaLista(ListaDiElementi->next); //struttura autoreferenziata
    }
}

//Esercizio 3
int lunghezzaListaIterativa(struct El* ListaDiElementi){
    int lung=0;
    while (ListaDiElementi!=NULL){
        ListaDiElementi=ListaDiElementi->next;
        lung++;
    }
    return lung;
}

int lunghezzaListaRicorsiva(struct El* ListaDiElementi){
    if (ListaDiElementi==NULL){
      return 0;
    }else{
      return lunghezzaListaRicorsiva(ListaDiElementi->next)+1;
    }
}

int main(){
  int n;
  struct El* lista; //puntare al primo elemento della lista
  struct El* l;
  lista=NULL; /* si inizializza il puntatote a NULL */

  do{
    printf("Inserisci un numero naturale o -1 per terminare: ");
    scanf("%d", &n);
    if (n>=0) {
      if (lista==NULL){ /* si verifica se la lista ha il valore NULL */
        /* alloca in memoria lo spazio per una struttura */
        lista=(struct El*) malloc(sizeof(struct El));
        l=lista;
      }else{ /* se il valore lista è diverso da NULL */
        /* alloca uno spazio in memoria per una nuova struttura
        e assegna a l il puntatote */
        l->next=(struct El*) malloc(sizeof(struct El));
        l=l->next; /* il puntatore l prende il valore del puntatore dell'elemento successivo */
      }
      l->valore=n; /* l va a puntare a valore a cui si assegna il valore di n */
      l->next=NULL; /* l va a puntare a next a cui si assegna il valore di NULL */
    }   //realizza una catena con il primo elemento della lista
  } while (n>=0);
  l=lista; /* l prende il valore del primo elemento della lista */
  printf("numeri inseriti: \n");
  while (l!=NULL){
    printf("%d - %p \n", l->valore, l->next);
    l=l->next; /* il puntatore l prende il valore del puntatore dell'elemento successivo */
  }
  printf("\n");
  stampaLista(lista);
  printf("\n");
  printf("lunghezza Lista Iterativa: %d\n", lunghezzaListaIterativa(lista));
  printf("lunghezza Lista Ricorsiva: %d\n", lunghezzaListaRicorsiva(lista));
}
