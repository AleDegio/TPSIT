/*
Alessia De Giovannini
Esercizio 2
*/

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

typedef struct stack_node{
  char valore;
  struct stack_node* next;  //puntatote referenziato (puntare alla struttura stessa)
};
typedef struct stack_node *stack_node;

void push(struct stack_node** head, struct stack_node* element){
	if (&head==NULL){
        element->next = NULL;
		*head=element;
	}else{
		element->next=*head;
		*head=element;
	}
}

struct stack_node* pop(struct stack_node** head){
	struct stack_node* ret=*head;
	if(&head==NULL){
		return NULL;
	}else{
		*head=ret->next;
	}
	return ret;
}

void stampaLista(struct stack_node* l){  //inserire l'inizio della lista
    if(l!=NULL){    //ripeto finchè esiste un elemento successivo
        printf("%c \n",l->valore);    //stampo il valore dell'elemento della lista e l'indirizzo del successivo
        l=l->next; //passo all'elemento successivo della lista
        stampaLista(l); //passo all'elemento successivo
    }
    return;
}

int main(){
    struct stack_node* head=NULL;
    struct stack_node* element;
    struct stack_node* item;
    char stringa[1000];
    printf("\nInserire la stringa:  ");
    fflush(stdin);
    scanf("%s", stringa);
    int i=0;
    do{
        if(stringa[i]=='('||stringa[i]==')'||stringa[i]=='['||stringa[i]==']'||stringa[i]=='{'||stringa[i]=='}'){
            element = (struct stack_node*) malloc(sizeof(struct stack_node));
            element->valore=stringa[i];
            if(head==NULL){
                push(&head, element);
            }else
            {
                if(head->valore=='('&&element->valore==')'){
                    item=pop(&head);
                    free(item);
                }else if(head->valore=='['&&element->valore==']'){
                    item=pop(&head);
                    free(item);
                }else if(head->valore=='{'&&element->valore=='}'){
                    item=pop(&head);
                    free(item);
                }else{
                    push(&head, element);
                }
            }
        }
        i++;
    }while(stringa[i]!='\0');
    printf("\nfine caricamento \n");
    stampaLista(head);
    if(head==NULL){
        printf("le parentesi sono giuste");
    }
    fflush(stdin);
    getch();
    return 0;
 }
