/*
Alessia De Giovannini
Esercizi 456
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
int lunghezzaListaRicorsiva(struct El* ListaDiElementi){
    if (ListaDiElementi==NULL){
      return 0;
    }else{
      return lunghezzaListaRicorsiva(ListaDiElementi->next)+1;
    }
}

//Esercizio 4
void deallocaLista(struct El* ListaDiElementi){
    if (ListaDiElementi==NULL){
      printf ("//\n");
    }else{
      printf("%d - %p \n",ListaDiElementi->valore, ListaDiElementi->next);
      free(ListaDiElementi);
      deallocaLista(ListaDiElementi->next); //struttura autoreferenziata
    }
}

//Esercizio 5 con Irene Gabutti
void swap(struct El* a, struct El* b){
    int temp = a->valore;
    a->valore = b->valore;
    b->valore = temp;
}

void ordinaLista(struct El* ListaDiElementi){
    int swapped, i;
    struct El* ptr1;
    struct El* lptr=NULL;

    if (ListaDiElementi==NULL){
        return;
    }

    do{
        swapped=0;
        ptr1=ListaDiElementi;

        while (ptr1->next != lptr){
            if (ptr1->valore > ptr1->next->valore){
                swap(ptr1, ptr1->next);
                swapped=1;
            }
            ptr1=ptr1->next;
        }
        lptr=ptr1;
      }while (swapped);
      stampaLista(ListaDiElementi);
}

//Esercizio 6
El merge(struct El* l1, struct El* l2){
  struct El* nuovo=NULL;
  struct El* ris=NULL;
  int primaVolta=1;

  /*scorre le due liste*/
  while ((l1!=NULL) && (l2!=NULL)){
    if (primaVolta==1){
      nuovo=(struct El*) malloc(sizeof(struct El));
      ris=nuovo;
      primaVolta=0;
    }else{
      nuovo->next=(struct El*) malloc(sizeof(struct El));
      nuovo=nuovo->next;
    }
    if (l1->valore < l2->valore){
      nuovo->valore = l1->valore;
      l1=l1->next;
    }else{
      nuovo->valore = l2->valore;
      l2=l2->next;
    }
  }

  /*viene eseguito solo uno dei due cicli*/
  while (l1!=NULL){
    nuovo->next=(struct El*) malloc(sizeof(struct El));
    nuovo=nuovo->next;
    nuovo->valore = l1->valore;
    l1=l1->next;
  }

  while (l2!=NULL){
    nuovo->next=(struct El*) malloc(sizeof(struct El));
    nuovo=nuovo->next;
    nuovo->valore = l2->valore;
    l2=l2->next;
  }

  /*NULL va al fondo della lista*/
  if (nuovo!=NULL){
    nuovo->next=NULL;
    return ris;
  }
}


int main(){
  struct El* lista1; //puntare al primo elemento della PRIMA lista
  struct El* l1;
  lista1=NULL; /*si inizializza il puntatote a NULL*/
  struct El* lista2; //puntare al primo elemento della SECONDA lista
  struct El* l2;
  lista2=NULL; /*si inizializza il puntatote a NULL*/
  int n1;
  int n2;

  //inserimento della PRIMA lista
  do {
    printf("Inserisci un numero naturale della PRIMA lista o -1 per terminare: ");
    scanf("%d", &n1);
    if (n1>=0) {
      if (lista1==NULL){ /* si verifica se la lista ha il valore NULL */
        /* alloca in memoria lo spazio per una struttura */
        lista1=(struct El*) malloc(sizeof(struct El));
        l1=lista1;
      }else{ /* se il valore lista è diverso da NULL */
        /* alloca uno spazio in memoria per una nuova struttura
        e assegna a l il puntatote */
        l1->next=(struct El*) malloc(sizeof(struct El));
        l1=l1->next; /* il puntatore l prende il valore del puntatore dell'elemento successivo */
      }
      l1->valore=n1; /* l va a puntare a valore a cui si assegna il valore di n */
      l1->next=NULL; /* l va a puntare a next a cui si assegna il valore di NULL */
    }   //realizza una catena con il primo elemento della lista
  } while (n1>=0);
  l1=lista1; /* l prende il valore del primo elemento della lista */
  printf("numeri inseriti PRIMA lista: \n");
  while (l1!=NULL){
    printf("%d - %p \n", l1->valore, l1->next);
    l1=l1->next; /* il puntatore l prende il valore del puntatore dell'elemento successivo */
  }

  //inserimento della SECONDA lista
  do{
    printf("Inserisci un numero naturale della SECONDA lista o -1 per terminare: ");
    scanf("%d", &n2);
    if (n2>=0) {
      if (lista2==NULL){ /* si verifica se la lista ha il valore NULL */
        /* alloca in memoria lo spazio per una struttura */
        lista2=(struct El*) malloc(sizeof(struct El));
        l2=lista2;
      }else{ /* se il valore lista è diverso da NULL */
        /* alloca uno spazio in memoria per una nuova struttura
        e assegna a l il puntatote */
        l2->next=(struct El*) malloc(sizeof(struct El));
        l2=l2->next; /* il puntatore l prende il valore del puntatore dell'elemento successivo */
      }
      l2->valore=n2; /* l va a puntare a valore a cui si assegna il valore di n */
      l2->next=NULL; /* l va a puntare a next a cui si assegna il valore di NULL */
    }   //realizza una catena con il primo elemento della lista
  } while (n2>=0);
  l2=lista2; /* l prende il valore del primo elemento della lista */
  printf("numeri inseriti SECONDA lista: \n");
  while (l2!=NULL){
    printf("%d - %p \n", l2->valore, l2->next);
    l2=l2->next; /* il puntatore l prende il valore del puntatore dell'elemento successivo */
  }

  printf("\n");
  printf("lunghezza PRIMA lista Ricorsiva: %d\n", lunghezzaListaRicorsiva(lista1));
  printf("\n");
  printf("PRIMA lista ordinata: \n");
  ordinaLista(lista1);
  printf("\n");
  printf("\n");
  printf("lunghezza SECONDA lista Ricorsiva: %d\n", lunghezzaListaRicorsiva(lista2));
  printf("\n");
  printf("SECONDA lista ordinata: \n");
  ordinaLista(lista2);
  printf("\n");
  merge(lista1, lista2);
  printf("\n");
  deallocaLista(lista1);
  deallocaLista(lista2);
  return 0;
}
