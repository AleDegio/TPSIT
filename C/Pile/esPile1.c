/*
Alessia De Giovannini
Esercizio 1
*/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

typedef struct stack_node{
  int element;
  struct stack_node* next;  //puntatote referenziato (puntare alla struttura stessa)
};
typedef struct stack_node *stack_node;

int is_empty(struct stack_node* head){
  if(head==NULL){
    return 1;
  }else{
    return 0;
  }
}

void push(struct stack_node** head, struct stack_node* element){
  if(is_empty(*head)){
    *head=element;
    element->next=NULL;
  }else{
    element->next=*head;
    *head=element;
  }
}

struct stack_node* pop(struct stack_node** head) {
  struct stack_node* ret=*head;

  if(is_empty(*head)){
    return NULL;
  }else{
    *head=ret->next;
    return ret;
  }
}

bool verificaNum(char num[]){    //controllo se il numero supera le cifre max
    char possibiliNumeri[11]="0123456789";
    int i, j;
    bool vary=true;
    for(i=0; num[j]!='\0'; i++){
        for(j=0; j<11; j++){
            if(num[j]==possibiliNumeri[j]){
               vary=false;
            }
        }
        if(vary!=false){
            return false;
        }else{
            vary=true;
        }
    }
    return true;
}

void stampa(struct stack_node** head){
    struct stack_node *ret;
    int k=1;
    printf("Pila Caricata: ");
    ret=pop(head);
    while(ret!=NULL){
        printf("\nValore [%d]: %d", k, ret->element);
        k++;
        free(ret);  //libero lo spazio in memoria
        ret=pop(head);  //legge il prossimo elemento
    }
    return;
}

int main(int argc, char const *argv[]) {
  struct stack_node* head=NULL;
  struct stack_node* e;
  char num[1000];
  int k=0;  //contatore per caratteri stringa

  do {
    printf("Inserisci il numero: ");
    scanf("%s", &num);
  } while(!verificaNum(num));

  do{
      e=(struct stack_node*) malloc(sizeof(struct stack_node));   //allocazione dello spazio in memoria per il puntatore
      e->element=num[k]-48;    //aggiornare il valore di num (si tolglie 48 per il codice ASCII)
      k++;
      push(&head, e);    //aggiunge l'elemento alla mia pila
  }while(num[k]!='\0');

  stampa(&head);
  return 0;
}
