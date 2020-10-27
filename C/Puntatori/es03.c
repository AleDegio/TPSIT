/*
Alessia De Giovannini
Esercizio 3
*/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define LUNG 20   //lunghezza max di char

int main() {
  char st[LUNG];
  int i=0;
  char *p;

  printf("Inserisci la stringa (senza spazi, lunghezza massima = 40): ");
  scanf("%s", st);

  p=st;
  while (*p!='\0') {
    i++;
    p++;
  }

  printf("La lunghezza della stringa e' %d", i);
  return 0;
}
