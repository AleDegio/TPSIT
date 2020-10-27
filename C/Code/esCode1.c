/*
Alessia De Giovannini
Esercizio 1
*/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

typedef struct queue_node{
  int valore;
  struct queue_node* next;  //puntatote referenziato (puntare alla struttura stessa)
}queue_node;

void enqueue(struct queue_node** head, struct queue_node** tail, struct queue_node* element){
  if(*head==NULL){
		*head=element;
	}else{
		(*tail)->next=element;
	}
  *tail=element;
  element->next=NULL;

  printf("tail: %d \n", (*tail)->valore);
  printf("head: %d \n", (*head)->valore);
  printf("element: %d \n", element->valore);
}

struct queue_node* dequeue(struct queue_node** head, struct queue_node** tail) {
  struct queue_node* ret=*head;
	if(*head==NULL){
		return NULL;
    //printf("prima printf\n");
	}else{
		*head=ret->next;
    //printf("seconda printf\n");
	}
	if(*head==NULL){
		*tail=NULL;
    //printf("terza printf\n");
	}
  //printf("quarta printf\n");
	return ret;
}

/*void stampa(struct queue_node* head, struct queue_node* tail){
  while (tail!=NULL) {
    printf("tail: %d \n", tail->valore);
    printf("head: %d \n", head->valore);
    tail=tail->next;
    head=head->next;
  }
}
*/

void stampa(struct queue_node* head){
    while (head!=NULL){
      printf("%d -> ", head->valore);
      head=head->next;
    }
}

int main(int argc, char const *argv[]) {
  struct queue_node* head=NULL;
  struct queue_node* tail=NULL;
  struct queue_node* e;
  int val;

  //head=(struct queue_node*) malloc(sizeof(struct queue_node));
  //tail=(struct queue_node*) malloc(sizeof(struct queue_node));
  do{
    e=(struct queue_node*) malloc(sizeof(struct queue_node));
    printf("Inserisci un elemento della coda o -1 per terminare: ");
    scanf("%d", &val);
    if (val>=0) {
      e->valore=val;
      enqueue(&head, &tail, e);    //aggiunge l'elemento alla coda
    }
  }while(val>0);


  printf("Stampa coda: \n");
  stampa(head);
  printf("\n");

  while(e!=NULL){
      e = dequeue(&head, &tail);
      //free(element);
  }
  //dequeue(&head, &tail);
  printf("Stampa coda vuota: \n");
  stampa(head);
  return 0;
}
