/*
Alessia De Giovannini
Esercizio 4
*/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define DIM 50    //lunghezza max di un vet di char

typedef struct Struttura{
  char nome[DIM];
  int num;
}Struttura;

int main() {
  Struttura *lista;
  int d=0;

  printf("Inserisci la dimensione della lista: ");
  scanf("%d", &d);

  //bisogna fare un casting (Struttura*) per fargli riconoscere il tipo
  lista=(Struttura*)malloc(d*sizeof(Struttura));

  printf("size of structure = %d\n", sizeof(Struttura));

  for(int i=0; i<d; i++) {
    char t[DIM];
    printf("%d = ", i);
    fflush(stdin);
    gets(t);
    strcpy((i+lista)->nome, t);
    (i+lista)->num = i;
  }

  for (int k=0; k<d; k++){
      printf("pointer list [%d]=%p\n", k, (lista+k));
  }

  for (int i=0; i<d; i++){
      printf("Struttura %d\n ", i);
      printf("nome: %s \t numero: %d", (lista+i)->nome , (lista+i)->num);
      printf("\n");
  }

  free(lista);  //libera la memoria occupata da lista
  getch();
  fflush(stdin);
  return 1;
}
